def get_extraction_prompt(content: str):
    """
    Returns the exact extraction prompt for GPT processing.
    The function maintains the original prompt without any modifications.
    """

    is_case_study = "case study" in content.lower()

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
        
        - 'suggested_answer' (as an array of points)
        - 'case_study_context' (if applicable)

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
        - 'suggested_answer' (as an array of points)

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


[
{
    "suggested_answer": "Return on Investment (ROI): Measures the profitability of the affiliate marketing campaigns, calculated by comparing the revenue generated from affiliate sales to the cost of running the affiliate program. Conversion Rate: The percentage of users who take a desired action (e.g., make a purchase) after clicking on an affiliate link, indicating the effectiveness of affiliate traffic in driving sales. Average Order Value (AOV): The average amount spent by customers who purchase through affiliate links, helping to assess the value affiliates bring to each transaction. Cost per Acquisition (CPA): The total cost associated with acquiring a new customer through affiliate marketing efforts, vital for evaluating the cost-effectiveness of the affiliate program. Customer Lifetime Value (CLTV): Represents the total revenue a business can expect from a single customer account throughout their relationship, helping to understand the long-term value of acquiring customers via affiliates. Affiliate Share of Voice (SoV): Analyzes the visibility and influence of an organization's affiliates compared to competitors within the same niche or industry, highlighting the market positioning.",
    "question": "Identify and explain 2 performance metrics as the criteria to review affiliate marketing from an organization’s point of view.",
    "comparison_count": 2,
    "temperature": 1.54,
    "student_answer": "hhhhhhh",
    "marks": 10,
    "provider": "gemini",
    "model": "gemini-pro"
}
]
