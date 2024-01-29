# Short-Form Script Generator

The Short-Form Script Generator is an AI-powered application designed to generate creative and engaging voiceover scripts for short-form video content. Leveraging the capabilities of OpenAI's GPT models, this tool provides users with unique scripts that evoke specific emotions, tailored for short video formats.

## Features

- Generate single or multiple voiceover scripts.
- Customise scripts to target specific emotions: Happiness, Anger, Love.
- Evaluate and classify generated scripts based on emotion using Hugging Face transformers.

## Getting Started

Follow these instructions to set up the Short-Form Script Generator on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.6 or higher
- pip

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/short-form-script-generator.git](https://github.com/3zz3/short-form-script-generator.git
   cd short-form-script-generator
   ```

2. **Install Required Python Packages**

   Install all the necessary Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **OpenAI API Key**

   You need an API key from OpenAI to use their GPT models. Once you have your API key, replace the placeholder in `config.json` with your actual API key.

   ```json
   {
     "OPENAI_KEY": "your_openai_api_key_here"
   }
   ```

   > **Note:** Keep your API key secure and do not share it publicly.

### Usage

To run the application, navigate to the project directory and execute the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server, and your default web browser should open the application automatically. If it doesn't, you can manually navigate to the URL provided in the terminal.

## Contributing

Contributions to the Short-Form Script Generator are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## License

This project has been created for demo purposes.

## Screenshots of the Demo

![Screenshot 2024-01-29 at 15 20 38](https://github.com/3zz3/short-form-script-generator/assets/63882209/d3d10125-5fd3-4c0b-a302-de16074f4188)
![Screenshot 2024-01-29 at 14 06 49](https://github.com/3zz3/short-form-script-generator/assets/63882209/3ac37232-322c-490c-ad4a-27cede1e8d38)

