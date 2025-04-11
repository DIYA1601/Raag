from flask import Flask, render_template, request
from models.skill_matcher import get_recommendations
from utils.tips_generator import get_resume_tips, get_interview_tips

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_skills = request.form.get("skills")
        skills_list = [skill.strip().lower() for skill in user_skills.split(",")]
        recommendations = get_recommendations(skills_list)
        resume_tips = get_resume_tips()
        interview_tips = get_interview_tips()
        return render_template("index.html", recommendations=recommendations,
                               resume_tips=resume_tips, interview_tips=interview_tips)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
