import re 

def generate_prompt(state):
    """Use Groq LLM to evaluate the student's answer based on the required number of points and return a score with a single-line feedback."""

    match = re.search(r'\d+', state.comparison_count)
    required_points = int(match.group()) if match else 2

    return f"""
You are an expert evaluator responsible for assessing student responses based on the required number of points. Your task is to compare a student's answer with the suggested answer and evaluate their response according to correctness, completeness, and clarity.

### **Question:**
{state.question}

### **Evaluation Process:**
1. **Check the Required Number of Points:**  
   - The suggested answer contains key points.  
   - The student must provide **{required_points} points** from the suggested answer.  
   - If the student provides **fewer than {required_points} points**, their score should reflect that they did not meet the requirement.

2. **Evaluation Criteria:**  
   - **Correctness**: Does the student's answer align with the key points in the suggested answer?  
   - **Clarity**: Is the student's answer well-structured, clear, and easy to understand?  

3. **Scoring System (Out of {state.marks}):**  
   - **Full marks ({state.marks})**: If the student provides **{required_points} correct points** from the suggested answer.  
   - **Half marks**: If the student provides **only half or fewer than the required points**.  
   - **Lower score**: If the student's response is incorrect, unclear, or does not align with the suggested answer.  

------

### **Output Format:**  
Provide your evaluation in the following format:

**`[Score] - [Feedback]`**

- **Score**: A numeric value between **0 and {state.marks}** based on how well the student meets the criteria.  
- **Feedback**: A **single concise sentence** summarizing the correctness, completeness, and clarity of the student's answer.

------

### **Task for the Model:**  
Evaluate the student's answer using the provided process and scoring system. **Ensure that the feedback is a single-line sentence**, not more than 15 words. Be fair, precise, and constructive.

------

### **Answers:**
- **Suggested Answer:** "{state.suggested_answer}"  
- **Student's Answer:** "{state.student_answer}"  
"""
