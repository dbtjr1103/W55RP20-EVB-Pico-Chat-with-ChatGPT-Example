import json
import time
from machine import Pin, WIZNET_PIO_SPI
import network
import urequests

# API 관련 설정
api_key = "[YOUR-API-KEY]"
chatgpt_url = "https://api.openai.com/v1/chat/completions"
chatgpt_ver = "gpt-4o-mini"
end_command = ">exit"

# 이더넷 초기화 함수
def init_ethernet(timeout=10):
    spi = WIZNET_PIO_SPI(baudrate=31_250_000, mosi=Pin(23), miso=Pin(22), sck=Pin(21))  # W55RP20 PIO_SPI
    nic = network.WIZNET5K(spi, Pin(20), Pin(25))  # spi, cs, reset pin
    nic.active(True)
    
    # 수동 IP 설정
    nic.ifconfig(('192.168.0.20', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    
    # 연결 대기
    start_time = time.time()
    while not nic.isconnected():
        time.sleep(1)
        if time.time() - start_time > timeout:
            raise Exception("Ethernet connection timed out.")
        print('Connecting ethernet...')

    print(f'Ethernet connected. IP: {nic.ifconfig()}')

# ChatGPT API 호출 함수 (재시도 기능 추가)
def send_prompt_to_chatGPT(prompt, retries=3):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": f"{chatgpt_ver}",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    for attempt in range(retries):
        try:
            response = urequests.post(chatgpt_url, headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                response_data = json.loads(response.text)
                return response_data["choices"][0]["message"]["content"]
            else:
                print(f"API error ({response.status_code}): {response.text}")
        except Exception as e:
            print(f"Request failed: {e}")
        
        # 재시도 전 대기
        time.sleep(2)
    
    raise Exception("Failed to get a response from ChatGPT after several retries.")

# ChatGPT와 상호작용 함수 (입력 예외 처리 추가)
def chat_with_chatGPT():
    while True:
        try:
            prompt = input("user: ")
            if prompt.strip().lower() == end_command:
                print("Exiting chat...")
                break

            response = send_prompt_to_chatGPT(prompt)
            print(f">gpt-4: {response}")
        except KeyboardInterrupt:
            print("\nChat interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"Error during chat: {e}")

# 메인 함수
def main():
    try:
        init_ethernet()
        chat_with_chatGPT()
    except Exception as e:
        print(f"Fatal error: {e}")

if __name__ == "__main__":
    main()

