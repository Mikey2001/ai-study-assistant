# AI Study Assistant

AI-assisted study assistant using an agent-based approach with search and calculator tools.

---

## Step 1 – System Planning (24.04)

### 1. System Description
The planned system is an AI-assisted study assistant implemented in Python. The goal of the system is to help users answer academic or general questions by processing user input and generating structured responses. The system will use an intelligent agent that can decide how to handle the input and use external tools when necessary to produce accurate results.

---

### 2. AI / Agent-Based Approach
The system will be implemented as a single intelligent agent. The agent will receive user input, analyze the request, and decide which tool to use in order to generate the response. The agent will simulate intelligent behavior by selecting between different tools such as a search function or a calculator.

---

### 3. Tools Used in the System
The system will include the following tools:

- A search tool for retrieving information based on user queries  
- A calculator tool for performing mathematical operations  

---

### 4. Preliminary Programming Concepts
The following programming concepts will be used:

- Python classes and objects  
- Functions and modular programming  
- Conditional statements (if-else logic)  
- Exception handling  
- Input and output handling  
- Basic string processing

- ---

## Step 2 – Implementation Progress (08.05)

### Updated System Description
The system has been partially implemented as an AI-assisted study assistant. The agent processes user input and determines whether to perform a calculation or retrieve information.

### Programming Concepts Used
- Classes and objects
- Functions
- Conditional statements
- Exception handling
- Modular programming


---

## Step 3 – Testing and Deployment Preparation (15.05)

### 1. Testing Process
Testing was performed during development to ensure that each module works correctly. The system was tested manually using different input scenarios. Each tool was tested separately, followed by testing of the full agent workflow.

---

### 2. Test Scenarios

#### Valid calculation
Input:
```text
calculate 2+2
```

Expected Output:
```text
Result: 4
```

---

#### Invalid calculation
Input:
```text
calculate abc
```

Expected Output:
```text
Error: Invalid mathematical expression
```

---

#### Information query
Input:
```text
What is Python?
```

Expected Output:
```text
Python is a high-level programming language.
```

---

#### Empty input
Input:
```text

```

Expected Output:
```text
Please enter a valid question.
```

---

### 3. Deployment Preparation
The system is prepared as a local command-line application.

To run the system:

```bash
python main.py
```

The project dependencies are listed in requirements.txt.

---

### 4. Data Conversion / Porting
The system receives user input as plain text. The agent processes the text and determines whether the input should be passed to the calculator tool or the search tool.

For calculations, the text is converted into a mathematical expression before evaluation.

The output from each tool is returned as a formatted string to the user.### Tool Integration
The tools are implemented as separate modules and imported into the agent. The agent selects which tool to use based on user input.


---

# Final Submission (22.05)

## Final System Description

The final system is an AI-assisted study assistant developed in Python for first-year university students studying introductory programming and computer science. The system helps users solve beginner-level academic tasks related to Python programming, algorithms, and mathematical calculations.

Users can ask questions such as:
- “What is a loop in Python?”
- “Explain sorting algorithms”
- “calculate 5 * (3 + 2)”

The system generates structured responses including explanations, definitions, code examples, and calculation results.

---

## Final AI / Agent-Based Approach

The system is implemented as a single intelligent agent using rule-based Natural Language Processing (NLP) techniques.

The agent analyzes user input using:
- keyword matching
- intent classification
- pattern recognition

Inputs related to calculations activate the calculator tool, while programming-related questions activate the search tool.

If the input is unclear, the system uses fallback intent detection to select the most relevant category.

---

## Final Tools and Their Roles

### Calculator Tool
Processes mathematical expressions and returns formatted calculation results.

### Search Tool
Provides educational information related to Python programming, algorithms, and beginner-level computer science concepts.

### Agent Logic
Controls the workflow by analyzing user input and selecting the appropriate tool.

---

## Final Programming Concepts

The project uses:
- Classes and objects
- Functions and modular programming
- Conditional statements
- Exception handling
- Input validation
- File and folder organization

---

## Final Testing Results

### Test Scenarios

| Input | Expected Output |
|---|---|
| calculate 2+2 | Result: 4 |
| calculate abc | Error message |
| What is Python? | Python explanation |
| What is an algorithm? | Algorithm definition |
| Empty input | Validation message |

### Conclusions

Testing confirmed that the system correctly processes user input, selects the appropriate tool, and handles invalid input safely.

---

## Deployment Preparation

The system is prepared as a local command-line application.

### Running the system

```bash
python main.py
```

---

## Data Conversion / Porting

The system receives plain text input from the user.

- Mathematical input is converted into evaluable expressions for the calculator tool.
- Programming-related questions are matched against predefined educational content in the search tool.

The results are formatted and returned as readable text responses.

---

## Deployment Strategy

The system is designed as a lightweight local application suitable for beginner-level educational use.

In the future, the project could be extended into:
- a web application using Flask or FastAPI,
- an API-based assistant,
- or a web-based educational chatbot.
