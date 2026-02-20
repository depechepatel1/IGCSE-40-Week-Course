import csv
import json

# Define the data for Weeks 3, 4, 5
# Note: Colors and styles follow Week 1 template:
#   <mark style="background-color: yellow;">Yellow complex sentence</mark>
#   <span style="color: blue;">Blue sentence starters</span>
#   <strong>Bold vocabulary</strong>

# CORRECTED Recycled Words:
# Week 3 Recycled: Informative, Addictive
# Week 4 Recycled: Consume, Nutritious
# Week 5 Recycled: Congestion, Convenient

weeks_data = [
    {
        "week_number": 3,
        "unit_title": "Food & Diet (Unit 3)",
        "walt_content": "Describe memorable meals and eating habits using specific vocabulary. Use the Present Perfect Tense to talk about life experiences with food.",
        "wilf_content": "1. Exactly ONE <mark style=\"background-color: yellow;\">yellow complex sentence</mark>.<br><br>2. At least TWO <span style=\"color: blue;\">blue sentence starters</span>.<br><br>3. Accurate use of the <strong>bold</strong> weekly vocabulary.",
        "support_content": "Sentence frames: <em>\"My favorite meal is ____ because...\"</em> and <em>\"I have never eaten ____.\"</em> rely on Chinese translation table.",
        "stretch_content": "Use sensory adjectives (spicy, bitter, crunchy) to describe food in detail. Direct fast-finishers to Section 10.",
        "grammar_title": "Quantifiers & Present Perfect",
        "grammar_content": "<br><br>• <strong>Quantifiers:</strong> Use <em>too much</em> (uncountable) and <em>too many</em> (countable). (e.g., <em>I ate too much cake / too many cookies</em>).<br><span style=\"color: #7f8c8d; font-size: 0.9em;\">量词：too much + 不可数名词; too many + 可数名词</span><br><br>• <strong>Present Perfect:</strong> Use <em>have/has + V3</em> for experiences. (e.g., <em>I have tried sushi before.</em>).<br><span style=\"color: #7f8c8d; font-size: 0.9em;\">现在完成时：have/has + 过去分词，表示经历</span>",
        "pronunciation_title": "Long Vowel Sounds",
        "pronunciation_content": "<br><br>Stretch out the vowel sounds in words like <em>food</em> (fuuuud), <em>eat</em> (eeet), and <em>meal</em> (meeeal). Do not cut them short!<br><span style=\"color: #7f8c8d; font-size: 0.9em;\">长元音：拉长元音发音，不要读得太短促！</span>",
        "vocab_rows": json.dumps([
            {"word": "Nutritious", "type": "Adj", "meaning": "\u6709\u8425\u517b\u7684"},
            {"word": "Ingredient", "type": "N", "meaning": "\u98df\u6750 / \u914d\u6599"},
            {"word": "Cuisine", "type": "N", "meaning": "\u83dc\u80b4 / \u70f9\u996a"},
            {"word": "Consume", "type": "V", "meaning": "\u6d88\u8017 / \u5403\u559d"},
            {"word": "Appetite", "type": "N", "meaning": "\u80c3\u53e3 / \u98df\u6b32"},
            {"word": "Homemade", "type": "Adj", "meaning": "\u81ea\u5236\u7684"}
        ]),
        "recycled_words_note": "Informative, Addictive",
        "idioms": json.dumps([
            {"phrase": "Have a sweet tooth", "meaning": "\u55dc\u751c\u5982\u547d / \u559c\u98df\u751c\u98df", "explanation": "\u6781\u5176\u559c\u6b22\u5403\u7cd6\u679c\u3001\u751c\u70b9\u7b49\u751c\u98df\u3002", "example": "I have a sweet tooth, so I always order chocolate cake after dinner.", "bg_color": "#fef9e7"},
            {"phrase": "A piece of cake", "meaning": "\u5c0f\u83dc\u4e00\u789f / \u6613\u5982\u53cd\u638c", "explanation": "\u5f62\u5bb9\u505a\u67d0\u4ef6\u4e8b\u60c5\u975e\u5e38\u5bb9\u6613\uff0c\u6beb\u4e0d\u8d39\u529b\u3002", "example": "For a professional chef, cooking a big family dinner is a piece of cake.", "bg_color": "#e8f8f5"}
        ]),
        "warmup_questions": json.dumps([
            "(Section 5 Question) <strong>What is the most <em>entertaining</em> cooking show you have ever watched?</strong> (Recycled vocab)",
            "Do you prefer <strong>homemade</strong> food or eating out at restaurants?",
            "Have you ever tried to cook a <strong>nutritious</strong> meal by yourself?"
        ]),
        # Week 3 Recycled: Informative, Addictive
        "transcoded_input": "<span style=\"color: blue;\">To be honest,</span> I have always had a huge <strong>appetite</strong>. <span style=\"color: blue;\">Recently,</span> I watched an <strong>informative</strong> documentary about sugar, and I learned that it is very <strong>addictive</strong>. <span style=\"color: blue;\">However,</span> I <strong>have a sweet tooth</strong>, so it is hard for me to stop eating cakes. <span style=\"color: blue;\">Usually,</span> I try to <strong>consume</strong> healthy <strong>ingredients</strong> like vegetables and fish. <mark style=\"background-color: yellow;\">Although fast food is tasty, I know that <strong>homemade</strong> food is much more <strong>nutritious</strong>.</mark> <span style=\"color: blue;\">Actually,</span> I have tried Japanese <strong>cuisine</strong> many times, and I love it. <span style=\"color: blue;\">Overall,</span> cooking healthy food is not <strong>a piece of cake</strong>, but it is worth it.",
        "circuit_prompt_intro": "Describe a memorable meal you have had. You should say:",
        "circuit_prompt_points": json.dumps([
            "Where you had it and who you were with.",
            "What specific dishes and ingredients you ate.",
            "Explain why this meal was so memorable for you."
        ]),
        "spider_center": "Memorable Meal",
        "spider_leg_1": "Location & Company",
        "spider_leg_2": "Food & Ingredients",
        "spider_leg_3": "Flavors & Taste",
        "spider_leg_4": "Why Memorable?",
        # Week 3 Recycled: Informative, Addictive
        "model_answer": "<span style=\"color: blue;\">Well,</span> the most memorable meal I have ever had was a dinner at my grandmother's house. <span style=\"color: blue;\">Normally,</span> we visit her every Spring Festival. <span style=\"color: blue;\">Actually,</span> she is an amazing cook, and her <strong>homemade</strong> dumplings are delicious. <span style=\"color: blue;\">To be honest,</span> the <strong>ingredients</strong> she uses are always fresh from her garden. <mark style=\"background-color: yellow;\">Because the food was so <strong>nutritious</strong> and tasty, I <strong>consumed</strong> three huge bowls!</mark> <span style=\"color: blue;\">In fact,</span> I have such a big <strong>appetite</strong> when I am there. <span style=\"color: blue;\">To sum up,</span> traditional Chinese <strong>cuisine</strong> is my favorite, and eating with family is never <strong>a piece of cake</strong> to forget. Also, learning about her recipes was very **informative** and the taste was truly **addictive**.",
        "listener_task_content": "<strong>Peer Assessment:</strong> Tally how many <span style=\"color: blue;\">Blue starters</span> your partner uses.<br><br><strong>Action:</strong> Give them a \"thumbs-up\" when you hear their <mark style=\"background-color: yellow;\">Yellow complex sentence</mark>!<br><br><strong>Tally:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]",
        "fast_finisher_question": "Do people in your country eat healthier food now than in the past? Why?",
        "exit_ticket_content": "<strong>Fix the Error (Countable vs Uncountable):</strong> Circle the correct word.<br><br>1. I ate too ( much / many ) rice.<br><br>2. There are too ( much / many ) apples on the table.<br><br>3. She drinks too ( much / many ) water.",
        "pre_homework_task": "<strong>App Shadowing (10 Mins):</strong> Open the App. Listen to the <strong>Week 3 Vocabulary and Model Answer</strong>. Shadow their pronunciation of long vowel sounds.",
        "post_homework_task": "<strong>App Recording (10 Mins):</strong> Record a 2-minute audio answering this week's prompt. <strong>Requirement:</strong> Use 1 complex sentence and the Present Perfect tense."
    },
    {
        "week_number": 4,
        "unit_title": "Transport (Unit 4)",
        "walt_content": "Discuss journeys and transport modes. Use the First Conditional to talk about future travel possibilities.",
        "wilf_content": "1. Exactly ONE <mark style=\"background-color: yellow;\">yellow complex sentence</mark>.<br><br>2. At least TWO <span style=\"color: blue;\">blue sentence starters</span>.<br><br>3. Accurate use of the <strong>bold</strong> weekly vocabulary.",
        "support_content": "Sentence frames: <em>\"I usually travel by...\"</em> and <em>\"If I go to..., I will...\"</em>",
        "stretch_content": "Use adverbs of probability (definitely, probably) with the First Conditional.",
        "grammar_title": "First Conditional",
        "grammar_content": "<br><br>• <strong>First Conditional:</strong> If + Present Simple, ... will + Verb. (e.g., <em>If it rains, I will take the bus.</em>).<br><span style=\"color: #7f8c8d; font-size: 0.9em;\">第一条件句：If + 一般现在时, ... will + 动词原形 (例如: If it rains, I will take the bus.)</span>",
        "pronunciation_title": "Sentence Stress in Conditionals",
        "pronunciation_content": "<br><br>Stress the key words (verbs and nouns) in both parts of the sentence. Emphasize the result!<br><span style=\"color: #7f8c8d; font-size: 0.9em;\">条件句中的重音：重读句子两部分中的关键词 (动词和名词)。强调结果！</span>",
        "vocab_rows": json.dumps([
            {"word": "Commute", "type": "V/N", "meaning": "\u901a\u52e4 / \u4e0a\u4e0b\u73ed\u5f80\u8fd4"},
            {"word": "Congestion", "type": "N", "meaning": "\u62e5\u5835 / \u585e\u8f66"},
            {"word": "Convenient", "type": "Adj", "meaning": "\u65b9\u4fbf\u7684 / \u4fbf\u5229\u7684"},
            {"word": "Passenger", "type": "N", "meaning": "\u4e58\u5ba2"},
            {"word": "Reliable", "type": "Adj", "meaning": "\u53ef\u9760\u7684 / \u53ef\u4fe1\u8d56\u7684"},
            {"word": "Vehicle", "type": "N", "meaning": "\u8f66\u8f86 / \u4ea4\u901a\u5de5\u5177"}
        ]),
        "recycled_words_note": "Consume, Nutritious",
        "idioms": json.dumps([
            {"phrase": "Beat the traffic", "meaning": "\u9519\u5cf0\u51fa\u884c", "explanation": "\u63d0\u65e9\u51fa\u53d1\u4ee5\u907f\u5f00\u9053\u8def\u4ea4\u901a\u9ad8\u5cf0\u671f\u3002", "example": "We need to leave the house at 6 AM to beat the traffic.", "bg_color": "#fef9e7"},
            {"phrase": "Miss the boat", "meaning": "\u9519\u5931\u826f\u673a / \u5750\u5931\u673a\u5b9c", "explanation": "\u56e0\u4e3a\u884c\u52a8\u592a\u6162\u800c\u9519\u5931\u4e86\u826f\u673a\u3002", "example": "I forgot to buy the cheap train tickets yesterday, so I missed the boat.", "bg_color": "#e8f8f5"}
        ]),
        "warmup_questions": json.dumps([
            "(Section 5 Question) <strong>How do you usually <em>commute</em> to school every day?</strong>",
            "If you <strong>consume</strong> too much junk food before a long trip, how do you feel? (Recycled)",
            "Is the public transport in your city usually <strong>reliable</strong>?"
        ]),
        # Week 4 Recycled: Consume, Nutritious
        "transcoded_input": "<span style=\"color: blue;\">To be honest,</span> my daily <strong>commute</strong> to school is quite long. <span style=\"color: blue;\">Usually,</span> I take the subway because it is very <strong>convenient</strong>. <span style=\"color: blue;\">However,</span> during rush hour, there are too many <strong>passengers</strong>. <mark style=\"background-color: yellow;\">If I wake up late tomorrow, I will definitely miss the bus and be late for class.</mark> <span style=\"color: blue;\">Sometimes,</span> my father drives me in his <strong>vehicle</strong>, but the <strong>congestion</strong> is terrible. <span style=\"color: blue;\">Actually,</span> we always try to leave early to <strong>beat the traffic</strong>. <span style=\"color: blue;\">In my opinion,</span> taking the subway is more <strong>reliable</strong> than driving. Also, it's safer because I don't **consume** fuel or pollute the air, which is not very **nutritious** for the planet.",
        "circuit_prompt_intro": "Describe a long journey you have taken. You should say:",
        "circuit_prompt_points": json.dumps([
            "Where you went and how you traveled.",
            "What happened during the journey.",
            "Explain how you felt about the trip."
        ]),
        "spider_center": "Long Journey",
        "spider_leg_1": "Destination & Mode",
        "spider_leg_2": "Events on Trip",
        "spider_leg_3": "Feelings",
        "spider_leg_4": "Future Plans",
        # Week 4 Recycled: Consume, Nutritious
        "model_answer": "<span style=\"color: blue;\">Well,</span> last summer I went to Beijing by train. <span style=\"color: blue;\">Actually,</span> it was a very long journey, taking over five hours. <span style=\"color: blue;\">To be honest,</span> the train was very comfortable and spacious for every <strong>passenger</strong>. <span style=\"color: blue;\">However,</span> we almost <strong>missed the boat</strong> because we arrived at the station late! <mark style=\"background-color: yellow;\">If I visit Beijing again, I will definitely take the high-speed train to save time.</mark> <span style=\"color: blue;\">Fortunately,</span> the train was <strong>reliable</strong> and we arrived on time. <span style=\"color: blue;\">Overall,</span> despite the <strong>congestion</strong> near the station, it was a <strong>convenient</strong> way to travel. I also managed to **consume** a very **nutritious** meal on board.",
        "listener_task_content": "<strong>Peer Assessment:</strong> Tally how many <span style=\"color: blue;\">Blue starters</span> your partner uses.<br><br><strong>Action:</strong> Give them a \"thumbs-up\" when you hear their <mark style=\"background-color: yellow;\">Yellow complex sentence</mark>!<br><br><strong>Tally:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]",
        "fast_finisher_question": "How can cities solve traffic jams without building more roads?",
        "exit_ticket_content": "<strong>Fix the Error (Conditionals):</strong> Match the sentence halves.<br><br>1. If it rains tomorrow, ... &nbsp;&nbsp;&nbsp;&nbsp; A. I stay at home.<br>2. If it rains tomorrow, ... &nbsp;&nbsp;&nbsp;&nbsp; B. I will stay at home.<br>3. If it rained, ... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; C. I would stay at home.",
        "pre_homework_task": "<strong>App Shadowing (10 Mins):</strong> Open the App. Listen to the <strong>Week 4 Vocabulary and Model Answer</strong>. Focus on sentence stress in the conditional sentences.",
        "post_homework_task": "<strong>App Recording (10 Mins):</strong> Record a 2-minute audio answering this week's prompt. <strong>Requirement:</strong> Use 1 First Conditional sentence."
    },
    {
        "week_number": 5,
        "unit_title": "Holidays (Unit 5)",
        "walt_content": "Describe unforgettable trips and travel experiences. Use Past Continuous vs Past Simple to tell stories.",
        "wilf_content": "1. Exactly ONE <mark style=\"background-color: yellow;\">yellow complex sentence</mark>.<br><br>2. At least TWO <span style=\"color: blue;\">blue sentence starters</span>.<br><br>3. Accurate use of the <strong>bold</strong> weekly vocabulary.",
        "support_content": "Sentence frames: <em>\"I went to ____.\"</em> and <em>\"While I was walking, I saw...\"</em>",
        "stretch_content": "Use narrative tenses to create suspense or interest in your story.",
        "grammar_title": "Past Continuous vs. Past Simple",
        "grammar_content": "<br><br>• <strong>Past Continuous:</strong> Was/Were + V-ing (Background action).<br>• <strong>Past Simple:</strong> V-ed (Interrupted action).<br>• <em>While I was sleeping (continuous), the phone rang (simple).</em><br><span style=\"color: #7f8c8d; font-size: 0.9em;\">过去进行时 vs 一般过去时：正在进行的背景动作被打断 (例如: While I was sleeping, the phone rang.)</span>",
        "pronunciation_title": "Weak forms of 'was/were'",
        "pronunciation_content": "<br><br>In fast speech, 'was' sounds like /wəz/ and 'were' sounds like /wə/. Don't stress them!<br><span style=\"color: #7f8c8d; font-size: 0.9em;\">弱读：在快速语流中，was 读作 /wəz/，were 读作 /wə/。不要重读它们！</span>",
        "vocab_rows": json.dumps([
            {"word": "Destination", "type": "N", "meaning": "\u76ee\u7684\u5730"},
            {"word": "Accommodation", "type": "N", "meaning": "\u4f4f\u5bbf"},
            {"word": "Itinerary", "type": "N", "meaning": "\u884c\u7a0b / \u65c5\u6e38\u8def\u7ebf"},
            {"word": "Souvenir", "type": "N", "meaning": "\u7eaa\u5ff5\u54c1"},
            {"word": "Breathtaking", "type": "Adj", "meaning": "\u4ee4\u4eba\u53f9\u4e3a\u89c2\u6b62\u7684 / \u6781\u7f8e\u7684"},
            {"word": "Explore", "type": "V", "meaning": "\u63a2\u7d22 / \u63a2\u9669"}
        ]),
        "recycled_words_note": "Congestion, Convenient",
        "idioms": json.dumps([
            {"phrase": "Travel light", "meaning": "\u8f7b\u88c5\u7b80\u884c / \u8f7b\u88c5\u4e0a\u9635", "explanation": "\u51fa\u95e8\u65c5\u884c\u65f6\u5c3d\u91cf\u5c11\u5e26\u884c\u674e\u3002", "example": "I always travel light because I hate carrying heavy bags at the airport.", "bg_color": "#fef9e7"},
            {"phrase": "Off the beaten track", "meaning": "\u4eba\u8ff9\u7f55\u81f3 / \u4e16\u5916\u6843\u6e90", "explanation": "\u53bb\u504f\u50fb\u7684\u3001\u5f88\u5c11\u6709\u6e38\u5ba2\u53bb\u7684\u51b7\u95e8\u5730\u65b9\u3002", "example": "We found a beautiful small beach that was completely off the beaten track.", "bg_color": "#e8f8f5"}
        ]),
        "warmup_questions": json.dumps([
            "(Section 5 Question) <strong>What is your dream holiday <em>destination</em>?</strong>",
            "Is public transport <strong>convenient</strong> in your city for tourists? (Recycled)",
            "Do you prefer to plan a strict <strong>itinerary</strong> or just relax?"
        ]),
        # Week 5 Recycled: Congestion, Convenient
        "transcoded_input": "<span style=\"color: blue;\">To be honest,</span> I love traveling. <span style=\"color: blue;\">Last year,</span> I went to Yunnan, which is a popular <strong>destination</strong>. <span style=\"color: blue;\">While</span> I was looking for <strong>accommodation</strong> online, I found a small hotel <strong>off the beaten track</strong>. <span style=\"color: blue;\">However,</span> the traffic <strong>congestion</strong> on the way there was bad. <mark style=\"background-color: yellow;\">While I was hiking up the mountain, I saw the most <strong>breathtaking</strong> view of the clouds.</mark> <span style=\"color: blue;\">Actually,</span> I prefer to <strong>travel light</strong> so I can <strong>explore</strong> easily. <span style=\"color: blue;\">In the end,</span> I bought a beautiful <strong>souvenir</strong> for my mom. It was **convenient** to carry home.",
        "circuit_prompt_intro": "Describe an unforgettable trip you have taken. You should say:",
        "circuit_prompt_points": json.dumps([
            "Where you went and who you went with.",
            "What you did there.",
            "Explain why it was unforgettable."
        ]),
        "spider_center": "Unforgettable Trip",
        "spider_leg_1": "Location & People",
        "spider_leg_2": "Activities",
        "spider_leg_3": "Sights & Sounds",
        "spider_leg_4": "Why Special?",
        # Week 5 Recycled: Congestion, Convenient
        "model_answer": "<span style=\"color: blue;\">Well,</span> my most unforgettable trip was to Japan. <span style=\"color: blue;\">Actually,</span> I went there with my family two years ago. <span style=\"color: blue;\">To be honest,</span> we didn't plan a strict <strong>itinerary</strong>. <mark style=\"background-color: yellow;\">While we were walking through Kyoto, we discovered a <strong>breathtaking</strong> old temple.</mark> <span style=\"color: blue;\">Fortunately,</span> our <strong>accommodation</strong> was very <strong>convenient</strong> and close to the subway. <span style=\"color: blue;\">Also,</span> I bought a traditional fan as a <strong>souvenir</strong>. <span style=\"color: blue;\">To sum up,</span> we loved to <strong>explore</strong> the city, even though we got lost once! We barely avoided the traffic **congestion** on the way to the airport.",
        "listener_task_content": "<strong>Peer Assessment:</strong> Tally how many <span style=\"color: blue;\">Blue starters</span> your partner uses.<br><br><strong>Action:</strong> Give them a \"thumbs-up\" when you hear their <mark style=\"background-color: yellow;\">Yellow complex sentence</mark>!<br><br><strong>Tally:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]",
        "fast_finisher_question": "What is the cultural impact of commercializing pristine destinations?",
        "exit_ticket_content": "<strong>Fix the Error (Past Tenses):</strong> Correct the verbs.<br><br>1. While I (walk) __________, I (see) __________ a cat.<br><br>2. She (cook) __________ dinner when the phone (ring) __________.<br><br>3. They (play) __________ football when it (start) __________ to rain.",
        "pre_homework_task": "<strong>App Shadowing (10 Mins):</strong> Open the App. Listen to the <strong>Week 5 Vocabulary and Model Answer</strong>. Pay attention to the weak pronunciation of 'was' and 'were'.",
        "post_homework_task": "<strong>App Recording (10 Mins):</strong> Record a 2-minute audio answering this week's prompt. <strong>Requirement:</strong> Use at least one sentence with 'While I was V-ing...'."
    }
]

# Append to CSV
file_exists = False
try:
    with open('course_data.csv', 'r') as f:
        file_exists = True
except FileNotFoundError:
    pass

with open('course_data.csv', 'a', newline='', encoding='utf-8') as f:
    fieldnames = [
        "week_number", "unit_title", "walt_content", "wilf_content", "support_content",
        "stretch_content", "grammar_title", "grammar_content", "pronunciation_title",
        "pronunciation_content", "vocab_rows", "recycled_words_note", "idioms",
        "warmup_questions", "transcoded_input", "circuit_prompt_intro", "circuit_prompt_points",
        "spider_center", "spider_leg_1", "spider_leg_2", "spider_leg_3", "spider_leg_4",
        "model_answer", "listener_task_content", "fast_finisher_question", "exit_ticket_content",
        "pre_homework_task", "post_homework_task"
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()

    for week_data in weeks_data:
        writer.writerow(week_data)
        print(f"Appended Week {week_data['week_number']}")
