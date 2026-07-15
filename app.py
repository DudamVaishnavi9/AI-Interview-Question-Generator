import gradio as gr
import requests

BACKEND_URL = "http://127.0.0.1:8000/interview"


def interview(topic, difficulty, num_questions):

    if topic.strip() == "":
        return "Please enter a topic."

    try:

        response = requests.post(
            BACKEND_URL,
            json={
                "topic": topic,
                "difficulty": difficulty,
                "num_questions": int(num_questions)
            },
            timeout=60
        )

        if response.status_code == 200:
            return response.json()["questions"]

        return response.text

    except requests.exceptions.ConnectionError:
        return "Backend server is not running."

    except requests.exceptions.Timeout:
        return "Request timed out."

    except Exception as e:
        return str(e)


demo = gr.Interface(
    fn=interview,

    inputs=[
        gr.Textbox(
            label="Interview Topic",
            placeholder="Python, Java, Machine Learning..."
        ),

        gr.Dropdown(
            ["Easy", "Medium", "Hard"],
            value="Medium",
            label="Difficulty"
        ),

        gr.Slider(
            minimum=1,
            maximum=20,
            step=1,
            value=5,
            label="Number of Questions"
        ),
    ],

   outputs=gr.Textbox(
    label="Generated Questions",
    lines=18
),
    title="AI Interview Question Generator",

    description="""
Generate customized technical interview questions using Google's Gemini AI.
""",

    examples=[
        ["Python", "Easy", 5],
        ["Java", "Medium", 10],
        ["Machine Learning", "Hard", 8],
        ["System Design", "Hard", 6],
    ],

    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch()