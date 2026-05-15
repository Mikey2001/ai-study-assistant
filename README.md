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
