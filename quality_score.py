def calculate_quality_score(image_quality, complaint_quality):
    
    score = 0
    
    if image_quality == "Good":
        score += 50
    else:
        score += 10
        
    if complaint_quality == "Good":
        score += 50
    else:
        score += 10
        
    return score