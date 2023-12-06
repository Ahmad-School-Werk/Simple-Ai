import re

def analyze_sentence(sentence):
    # Patroonherkenning om te bepalen of het een present, past of foutieve zin is
    present_pattern = re.compile(r'\b(am|is|are|eat|eats|eating|visit|finish|watch|travel|play|rain|start|meet|cook|go|study|set|buy|call|learn|forget|arrive|dance|see|pass|snow|lose|bake|walk|play|find|fix|leave|visit|have|picnic|read|clean|forget|buy|travel|see|build|ride|attend|play|take|cat|visit|run|celebrate|receive|cut|watch|score|explain|sleep|draw|hike|cook|build|adopt|organize|hike|bake|visit|complete|adopt|interview|receive|attend|build|perform|buy|learn|go|fix|explore|attend|graduate)\b', re.IGNORECASE)
    past_pattern = re.compile(r'\b(was|were|walked|played|had|rained|started|met|cooked|went|studied|set|bought|called|learned|forgot|arrived|danced|saw|passed|snowed|lost|baked|walked|played|found|fixed|left|visited|had|picnicked|read|cleaned|forgot|bought|traveled|saw|built|rode|attended|played|took|caught|visited|ran|received|cut|scored|explained|slept|drew|hiked|cooked|built|received|organized|hiked|baked|visited|completed|adopted|interviewed|received|attended|built|performed|bought|learned|fixed|explored|attended)\b', re.IGNORECASE)

    if present_pattern.search(sentence):
        tense = 'present'
    elif past_pattern.search(sentence):
        tense = 'past'
    else:
        tense = 'error'

    # Patroonherkenning om te bepalen of het simple, continuous of perfect is
    simple_pattern = re.compile(r'\b(eat|eats|walks|played|started|cooked|studied|set|bought|called|learned|forgot|danced|saw|passed|lost|left|visited|had|picnicked|read|cleaned|forgot|bought|saw|built|ridden|attended|played|taken|visited|run|celebrated|received|cut|watched|scored|explained|slept|drawn|hiked|cooked|built|adopted|received|organized|baked|visited|completed|adopted|interviewed|received|attended|built|performed|learned|fixed|attended)\b', re.IGNORECASE)
    continuous_pattern = re.compile(r'\b(am|is|are|eating|playing|raining|starting|meeting|cooking|going|studying|setting|buying|calling|learning|forgetting|arriving|dancing|seeing|passing|snowing|losing|baking|walking|playing|finding|fixing|leaving|visiting|having|picnicking|reading|cleaning|forgetting|buying|traveling|seeing|building|riding|attending|playing|taking|visiting|running|celebrating|receiving|cutting|watching|scoring|explaining|sleeping|drawing|hiking|cooking|building|adopting|receiving|organizing|hiking|baking|visiting|completing|adopting|interviewing|receiving|attending|building|performing|buying|learning|going|fixing|exploring|attending)\b', re.IGNORECASE)
    perfect_pattern = re.compile(r'\b(have|has|had|visited|finished|watched|traveled|played|rained|started|met|cooked|gone|studied|set|bought|called|learned|forgot|arrived|danced|seen|passed|snowed|lost|baked|walked|played|found|fixed|left|visited|had|picnicked|read|cleaned|forgot|bought|traveled|seen|built|rode|attended|played|taken|visited|run|celebrated|received|cut|watched|scored|explained|slept|drew|hiked|cooked|built|adopted|received|organized|hiked|baked|visited|completed|adopted|interviewed|received|attended|built|performed|bought|learned|gone|fixed|explored|attended|graduated)\b', re.IGNORECASE)

    if simple_pattern.search(sentence):
        aspect = 'simple'
    elif continuous_pattern.search(sentence):
        aspect = 'continuous'
    elif perfect_pattern.search(sentence):
        aspect = 'perfect'
    else:
        aspect = 'error'

    return tense, aspect

# 100 zinnen
sentences = [
    "I visited London last summer.",
    "She finished her homework before dinner.",
    "We watched a movie yesterday.",
    "He traveled to Paris two months ago.",
    # ... voeg de overige zinnen hier toe
]

# Loop door elke zin en voer de analyse uit
for sentence in sentences:
    tense, aspect = analyze_sentence(sentence)
    print(f"Original Sentence: {sentence}")
    print(f"Tense: {tense}")
    print(f"Aspect: {aspect}")
    print("\n" + "="*50 + "\n")


"Simple Ai die van Ahmad Al Dibo Gemaakt"