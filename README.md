# W55RP20-EVB-Pico: Chat with ChatGPT Example

This project demonstrates the usage of the W55RP20-EVB-Pico evaluation board to establish an Ethernet connection and interact with OpenAI's ChatGPT API. The goal is to create a simple but functional chat interface between the user and ChatGPT, utilizing a hardware-based Ethernet module.

## Overview
The W55RP20-EVB-Pico is an evaluation board that combines the W5500 Ethernet controller and the RP2040 microcontroller, providing both the capabilities of a Raspberry Pi Pico and W5500 Ethernet. It offers a convenient way to develop projects that require wired network connectivity.

### Key Features of W55RP20-EVB-Pico
- **W55RP20 Microcontroller**: Combines the W5500 Ethernet controller with the RP2040 chip.
- **RP2040 Dual-Core Processor**: 133MHz Cortex M0+ dual-core processor.
- **Built-in Ethernet Support**: Hardwired TCP/IP stack supports up to 8 simultaneous sockets, supporting protocols like TCP, UDP, ICMP, IPv4, and more.
- **GPIO Pin Compatibility**: The pinout is similar to Raspberry Pi Pico, allowing compatibility with Pico-based projects.
- **Built-in RJ45 and Power-over-Ethernet (PoE) Support**.

For more detailed information, please refer to the official documentation below.

## Project Description
This project showcases:
- Initializing the Ethernet interface on the W55RP20-EVB-Pico.
- Making API requests to the OpenAI ChatGPT endpoint to perform conversations.

Using this setup, we are able to communicate with ChatGPT through the device, enabling an interactive conversation. The project can be extended to use other APIs or interact with other AI models and applications.

### Micropython Firmware
While some of our company's other products such as **Wiznet W5500-EVB-Pico** and **W5100S-EVB-Pico** have official firmware available on the [Micropython official website](https://micropython.org/download), the MicroPython firmware for **W55RP20-EVB-Pico** can currently be found [WIZnet-ioNIC](https://github.com/WIZnet-ioNIC/WIZnet-ioNIC-micropython) on github.

## Project Setup
### Required Hardware
- W55RP20-EVB-Pico Module.
- Ethernet cable.
- Power source via USB.

### Software Requirements
- Python / MicroPython support for RP2040.
- WIZNET_PIO_SPI for SPI communication.
- Libraries: `json`, `urequests`, `network`, `machine`.

### Running the Project
1. **Connect the Ethernet**: Plug an Ethernet cable into the W55RP20-EVB-Pico board.
2. **Clone the Code Repository**: Clone this repository to your local development environment.
3. **Configure the API Key**: Replace the `api_key` variable with your OpenAI API key.
4. **Load Firmware**: Make sure to flash the appropriate firmware to your W55RP20-EVB-Pico module.
5. **Run the Code**: Use a serial terminal or IDE to execute the `main.py` file.

### Code Explanation
- **Ethernet Initialization (`init_ethernet`)**: Establishes a wired network connection using the WIZNET5K library. This function ensures proper connection setup and retries if there are connection issues.
- **ChatGPT API Interaction (`send_prompt_to_chatGPT`)**: Manages API calls to the OpenAI server, sends user prompts, and receives ChatGPT's response. This function also includes retries in case of connection errors.
- **Chat Loop (`chat_with_chatGPT`)**: Provides a command-line interface where the user can type in questions and get responses from ChatGPT.

## Example Use Case
Once everything is set up, the device allows for interactive conversation with ChatGPT through a command line. Future enhancements could include:
- Using different AI models for various tasks, such as sentiment analysis, translation, or summarization.
- Automating routine tasks by integrating with other services, like weather APIs, stock market data, or home automation.
- Using additional libraries for advanced functionality, such as sending notifications based on ChatGPT responses.

## Future Plans
This simple demonstration can be a building block for more advanced applications:
- **Additional API Integrations**: Connect with other services (e.g., weather data, stock prices, home automation) for extended functionality.
- **Interactive AI Chatbots**: Utilize other large language models (LLMs) for domain-specific interactions, such as customer service, FAQ bots, or educational assistance.
- **Advanced LLM Usage**: Implement LLM-based functionalities like sentiment analysis, complex Q&A, and text generation for IoT and embedded device projects.

## How to Get Firmware
- [Micropython Official Website](https://micropython.org/download) for other Wiznet products.
- [WIZnet-ioNIC MicroPython Firmware on GitHub](https://github.com/WIZnet-ioNIC/WIZnet-ioNIC-micropython) for W55RP20-EVB-Pico.

## Contributing
Feel free to contribute to this project by opening issues and submitting pull requests. Future contributions could focus on expanding capabilities to use other APIs and leveraging more advanced AI features on this powerful hardware.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or further discussions, please contact us via [GitHub Issues](https://github.com/your-github-repo/issues).

## References
- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- [WIZnet Official W55RP20 Documentation](https://docs.wiznet.io/Product/ioNIC/W55RP20/w55rp20-evb-pico)

