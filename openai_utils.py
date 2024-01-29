# This file contains functions related to interacting with the OpenAI API.
import json
import openai
import logging
import time

# Load OpenAI API key from config.json
def load_openai_api_key(config_path='config.json'):
    try:
        with open(config_path) as f:
            config = json.load(f)
            openai.api_key = config['OPENAI_KEY']
    except Exception as e:
        logging.error(f"Failed to load OpenAI API key: {e}")
        raise

# Generate 1 script, using the model_prompt and configuring the model to preferences
def generate_voiceover(model_prompt, model="gpt-4", temperature=1, max_tokens=700):
    try:
        completion = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": model_prompt},
                {"role": "user", "content": "Generate 1 script"}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return completion.choices[0].message.content, None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None, e

# Generate more than 1 script, user allowed to decide in GUI, using the model_prompt and configuring the model to preferences
def generate_voiceovers(model_prompt, n, model="gpt-4", temperature=1, max_tokens=700):
    scripts_data = []
    for i in range(n):
        try:
            completion = openai.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": model_prompt},
                    {"role": "user", "content": "Generate 1 script"}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            script = completion.choices[0].message.content
            # Placeholder for emotion extraction and evaluation
            emotion = "Extracted Emotion"
            eval1, eval2, eval3 = "Evaluation 1", "Evaluation 2", "Evaluation 3"  # Placeholder
            scripts_data.append([script, emotion, eval1, eval2, eval3])
            logging.info(f"Script {i+1} generated.")
        except Exception as e:
            logging.error(f"Error generating script {i+1}: {e}")
            # Optionally, handle partial failure here
        time.sleep(1)  # To avoid hitting API rate limits
    return scripts_data
