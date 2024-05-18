def highFive(items):
    # Create a dictionary to store scores of each student
    scores = {}
    for id, score in items:
        if id not in scores:
            scores[id] = []
        scores[id].append(score)

    # Calculate the average of the top five scores for each student
    result = []
    for id, score_list in scores.items():
        # Sort the scores in descending order
        #score_list.sort(reverse=True)
        # Calculate the average of the top five scores
        average_score = sum(sorted(score_list)[-5:]) // 5
        result.append([id, average_score])

    return result

# Example usage:
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(highFive(items))  # Output: [[1, 87], [2, 88]]
