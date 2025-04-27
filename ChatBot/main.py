
import Batches
painting_data_batch_1 = Batches.painting_data_batch_1
painting_data_batch_2 = Batches.painting_data_batch_2
painting_data_batch_3 = Batches.painting_data_batch_3
painting_data_batch_4 = Batches.painting_data_batch_4
painting_data_batch_5 = Batches.painting_data_batch_5

all_painting_data = (painting_data_batch_1 + painting_data_batch_2 +
                    painting_data_batch_3 + painting_data_batch_4 +
                    painting_data_batch_5)


def chatbot():
    print("Welcome! Ask me about famous paintings (e.g., 'Who painted Starry Night?'). Type 'quit' to exit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        user_input_lower = user_input.lower()
        found_painting = None
        response = "Chatbot: Sorry, I don't have information on that painting or I didn't understand. Please try again." # Default response

        matched_title = ""
        for painting in all_painting_data:
            title_lower = painting['title'].lower()
            if title_lower in user_input_lower:
                 if len(title_lower) > len(matched_title):
                    found_painting = painting
                    matched_title = title_lower
                 elif found_painting is None:
                    found_painting = painting
                    matched_title = title_lower


        if found_painting:
            requested_info = 'description'
            info_value = found_painting['description']

            if any(keyword in user_input_lower for keyword in ["who painted", "artist", "painter", "by who", "who made"]):
                requested_info = 'artist'
                info_value = found_painting['artist']

            elif any(keyword in user_input_lower for keyword in ["when", "year", "date", "created"]):
                requested_info = 'year'
                info_value = found_painting['year']

            elif any(keyword in user_input_lower for keyword in ["describe", "tell me about", "what is", "about"]):
                 requested_info = 'description'
                 info_value = found_painting['description']

            response = f"Chatbot: The {requested_info} of '{found_painting['title']}' is: {info_value}"

        print(response)


chatbot()