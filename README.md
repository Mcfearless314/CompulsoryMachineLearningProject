# Compulsory Machine Learning Project

## Setup Instructions

1. **Clone the repository**  
   Begin by cloning this repository to your local machine.

2. **Install dependencies**  
   Navigate to the project directory and install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**  
   In the root directory of the project, create a `.env` file and add your API keys in the following format:

   ```
   MISTRAL_API_KEY=your_mistral_api_key
   API_KEY=your_tavily_api_key
   ```


## Running the Agent

To test the AI, run the `mistral_agent.py` file:

```bash
python mistral_agent.py
```

You will be prompted in the console to provide:

- A topic  
- A time period  
- A year  
- A minimum number of citations  

The agent will then search the web and return relevant articles, including:

- Title  
- Description  
- Link  

It will also generate an evaluation of the response using the Mistral agent.

## Re-running the Program

To run the program again, simply re-execute `mistral_agent.py`.




An evaluation of the first agents response will also be visible, created by the mistral_agent.

The program ends and can be run again by running the mistral_agent.py file again.
