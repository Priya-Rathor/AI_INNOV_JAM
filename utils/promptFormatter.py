import re 

def get_extraction_prompt(content: str):
    """
    Determines the type of assessment (case study or written assessment) and returns the structured extraction prompt.
    """

    is_case_study = bool(re.search(r'\bcase\s*study\b', content, re.IGNORECASE)) or "case study context" in content.lower()

    assessment_type = "case_study" if is_case_study else "written_assessment"

    if is_case_study:
        return f"""
        You are an assistant that extracts structured information from text. 
        Extract the case study context only once if the document is for a case study assessment. 
        Then extract all the questions and suggested answers in the specified format.

        Extract the case study context only once if the document is for a case study assessment. Then extract all the questions and suggested answers, and format them as a JSON array. Each item should have the following structure:
        - 'Total Duration, Duration, time - float (Give only number, do not add any unit name with the number example:- 30, 60, 120, etc.)'
        - 'Instructions to Candidate'
        - 'Question_number'
        - 'Question' (Extract the complete question, including all its parts. Ensure that multi-line or multi-part questions are fully captured.)
        - 'Question_instruction' (These instructions come after the question number. If instructions are enclosed in parentheses, extract them as they are.)
        - 'Suggested_answer' (Extract all points that are present in the suggested answer as an array. Ensure that **every point from the answer is fully captured**, including subpoints, explanations, and multi-paragraph content. If an answer contains bullet points, sub-bullets, or paragraph-based reasoning, **include them all**.)
        - 'Comparison_count - float' (This count will come after the **Suggested Answer Heading** if it is present. If **Comparison_count** is not explicitly mentioned, try to find it in the **question** itself. If it is missing in both places, return null.)
        - 'Comparison_instruction' (If not present, return null. This instruction will come after the **Suggested Answer Heading** (e.g., any 1, any 2, any 3, any one, any two, any three). If not found, return null.)
        - 'Case_study_context' (If applicable, extract the **entire case study context** and ensure that all necessary details are included.)

        **Important:**  
        - Ensure that the **Suggested_answer** field contains every single suggested point **without missing any details**.  
        - Extract all relevant answer points, including subpoints, multi-paragraph explanations, and bullet-based content.  
        - If the answer is split across multiple paragraphs or structured differently, **preserve the full answer** in its original format.  
        - **Do not summarize, shorten, or rephrase the answers**; keep them as they appear in the document.  
        - If a question contains multiple parts (e.g., sub-questions or steps), extract **each part completely** and structure it appropriately.  

        Example output format:
        {{
            "assessment_type": "case_study",
            "duration": <Duration>,
            "assessment_instruction": [<instructions_to_candidate_point_1>, <instructions_to_candidate_point_2>, ...],
            "case_study_context": "<case study content>",
            "questions_and_answers": [
                {{
                    "question_number": <question_number>,
                    "question": "<full_question_text>",
                    "question_instruction": "<question_instruction>",
                    "suggested_answer": [<answer_point_1>, <answer_point_2>, ...],
                    "comparison_count": <comparison_count>,
                    "comparison_instruction": <comparison_instruction>
                }}
            ]
        }}

        Document content:
        {content}
        """
    else:
        return f"""
        You are an assistant that extracts structured information from text. 
        Extract all the questions and suggested answers in the specified format.

        Extract all the questions and suggested answers, and format them as a JSON array. Each item should have the following structure:
        - 'Total Duration, Duration, time - float (Give only number, do not add any unit name with the number example:- 30, 60, 120, etc.)'
        - 'Instructions to Candidate'
        - 'Question_number'
        - 'Question' (Extract the full question, including all its components and sub-parts.)
        - 'Question_instruction' (These instructions come after the question number and are typically enclosed in parentheses.)
        - 'Suggested_answer' (Extract **all points** from the suggested answer as an array. Ensure every answer component is captured, including subpoints, multi-paragraph content, and detailed reasoning.)
        - 'Comparison_count - float' (If **Comparison_count** is present, extract it. If it is missing, look for it in the **question**. If it is not found in both places, return null.)
        - 'Comparison_instruction' (Extract any instructions after the **Suggested Answer Heading** (e.g., any 1, any 2, any 3, any one, any two, any three). If not found, return null.)

        **Important:**  
        - The **Suggested_answer** field must contain **every** answer point.  
        - Extract all answer subpoints, detailed explanations, and multi-paragraph content without omitting any details.  
        - **Do not summarize, truncate, or modify the original answer**; keep its full structure intact.  
        - If a question has multiple parts (e.g., step-by-step breakdowns or sub-questions), extract **each part completely** and maintain its structure.  

        Example output format:
        {{
            "assessment_type": "written_assessment",
            "duration": <Duration>,
            "assessment_instruction": [<instructions_to_candidate_point_1>, <instructions_to_candidate_point_2>, ...],
            "case_study_context": "",
            "questions_and_answers": [
                {{
                    "question_number": <question_number>,
                    "question": "<full_question_text>",
                    "question_instruction": "<question_instruction>",
                    "suggested_answer": [<answer_point0_1>, <answer_point_2>, ...],
                    "comparison_count": <comparison_count>,
                    "comparison_instruction": <comparison_instruction>
                }}
            ]
        }}

        Document content:
        {content}
        """
