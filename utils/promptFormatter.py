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
        -'Total Duration,Duration,time-flaot-(Give only number , do not add any unit name with the number example:- 30 ,60,120 etc)'
        -'instructions to Candidate'
        - 'question_number'
        - 'question'
        - 'question_instruction (These instruction come after question number. It is present in ())'
        -'comparison_count -flaot- (This count will come after the Suggested answer Handing give if it is present if comparison_count not present then try  to find it form the question. if there are not present both place then all )
        -'comparison_instruction(If not presnet then send null,This count will come after the Suggested answer Handing (any 1,any 2,any 3,any one,any two,any three) if not presnet then send null)
        - 'suggested_answer' (as an array of points, ensuring all details and explanations are fully captured, including multi-paragraph content if applicable)
        - 'case_study_context' (if applicable)

        **Important:**  
        - Ensure that the **suggested_answer** field contains the full, detailed answer.  
        - Extract all relevant answer points, including any subpoints or explanations.  
        - If the answer is split across multiple paragraphs or bullet points, include them all in the array.  
        - Do not summarize or truncate answers; keep the complete answer structure.  
        
        Example output format:
        {{
            "assessment_type": "case_study",
            "duration":<Duration>,
            "assessment_instruction":[<instructions to Candidate_point_1>, <instructions to Candidate_point_2>, ...],
            "case_study_context": "<case study content>",
            "questions_and_answers": [
                {{
                    "question_number": <question_number>,
                    "question": "<question_text>",
                    "question_instruction": "<question_instruction>",
                    "comparison_count":<comparison_count>,
                    "comparison_instruction":<comparison_instruction>,
                    "suggested_answer": [<answer_point_1>, <answer_point_2>, ...]
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
        -'Total Duration,Duration,time -flaot-(Give only number , do not add any unit name with the number example:- 30 ,60,120 etc)'
        -'instructions to Candidate'
        - 'question_number'
        - 'question'
        - 'question_instruction (These instruction come after question number. It is present in ())'
        -'comparison_count -flaot -(This count will come after the Suggested answer Handing give if it is present if comparison_count not present then try  to find it form the question. if there are not present both place then all )'
        -'comparison_instruction(If not presnet then send null,This count will come after the Suggested answer Handing (any 1,any 2,any 3,any one,any two,any three) if not presnet then send null)
        -'suggested_answer' (as an array of points, ensuring all details and explanations are fully captured, including multi-paragraph content if applicable)

        **Important:**  
        - Ensure that the **suggested_answer** field contains the full, detailed answer.  
        - Extract all relevant answer points, including any subpoints or explanations.  
        - If the answer is split across multiple paragraphs or bullet points, include them all in the array.  
        - Do not summarize or truncate answers; keep the complete answer structure.  


        Example output format:
        {{
            "assessment_type": "written_assessment",
            "duration":<Duration>,
            "assessment_instruction":[<instructions to Candidate_point_1>, <instructions to Candidate_point_2>, ...],
            "case_study_context": "",
            "questions_and_answers": [
                {{
                    "question_number": <question_number>,
                    "question": "<question_text>",
                    "question_instruction": "<question_instruction>",
                    "conparison_instruction":<comparison_instruction>,
                    "comparison_count":<comparison_count>,
                    "suggested_answer": [<answer_point_1>, <answer_point_2>, ...]
                }}
            ]
        }}

        Document content:
        {content}
        """



