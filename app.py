import script_generator_functions
import streamlit as st
from openai_utils import load_openai_api_key, generate_voiceovers, generate_voiceover
from data_processing import extract_text_from_pdf, save_to_excel
from ui_elements import generate_sidebar, display_script
import logging

# Main function
def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Load API keys and initialize services
    load_openai_api_key()

    # UI setup
    menu_choice = generate_sidebar()

    # Extract dataset text from PDF
    dataset_text = script_generator_functions.extract_text_from_pdf("data/scripts_dataset.pdf")

    # Construct the model prompt
    model_prompt = f"""
    You are an AI trained to generate creative and engaging voiceover scripts for short-form video content. Your task is 
    to read the provided example scripts, choose the target emotion, either love, anger or fear, and then produce a 
    voiceover script that vividly brings the scene to life while evoking the specified emotion. Each script should be 
    concise, engaging, and suitable for a short video format.

    For each task:
    1. Begin by reading the example scripts.
    2. Randomly pick the target emotion (Happiness, Anger, Love).
    3. Generate a voiceover script, [generated_script], that:
       - Accurately reflects the scene's setting and actions.
       - Clearly evokes the target emotion through tone, word choice, and narrative.
       - Is engaging and captures the audience's attention.
       - Fits within a short video format, aiming for a script length that would translate to roughly 30-60 seconds of spoken content.
    4. Generate a [script_title] that fits the [generated_script]

    Remember, your goal is to create a script that not only tells a story but also connects emotionally with the 
    audience, enhancing the visual experience with compelling narration.

    Example Scripts: 
    {dataset_text}

    ANSWER MUST FOLLOW THIS LAYOUT

    Title: [script_title]
    Emotion: [picked_emotion]
    Script: [generated_script]

    [generated_script] MUST FOLLOW THIS LAYOUT

    Start of the script

    Scene 1:

    Scene 2:

    Scene 3:

    End of Script
    """

    # Display items based on user's menu choice
    if menu_choice == "Script Generator":
        st.title("ScriptCraft: AI-Powered Short-Form Script Generation")

        # Streamlit UI for generating a single voiceover script
        if st.button("Generate Voiceover Script"):
            script, error = generate_voiceover(model_prompt)
            if script:
                st.text_area("Generated Script", script, height=300)
            else:
                st.error(f"An error occurred: {error}")

        # Streamlit UI for generating multiple voiceover scripts
        n = st.number_input("Number of scripts to generate", min_value=1, value=5)
        if st.button("Generate Multiple Voiceover Scripts"):
            progress_bar = st.progress(0)
            scripts_data = generate_voiceovers(model_prompt, n)
            for i, _ in enumerate(scripts_data, 1):
                progress_bar.progress(int(100 * i / n))
            # Save 100 scripts to excel
            save_to_excel(scripts_data)
            st.success("Scripts generated successfully.")
            # Further processing of scripts_data as needed

    elif menu_choice == "Metrics accuracy":
        # Page to display hugging face models accuracy scores - unable to complete, but these scores can be found in the
        # spreadsheet or in the Script Generator page
        st.title("Model Metrics Accuracy")
        st.error("Please see hugging face emotion-text-classification open source models accuracies in the Script Generator page or in the spreadsheet. As due to time constraints, this function is not yet available in Streamlit.")


if __name__ == "__main__":
    main()
