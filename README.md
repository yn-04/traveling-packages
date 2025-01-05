<h1 style="text-align: center;">Traveling Packages</h1>

## About the project

A web application for planning travel packages and creating image to promoting the province's landmark. This web application uses generative AI for creating travel packages (Text-to-Text) and image promoting (Text-to-Image).

## Contributors

<!-- readme: samslow,alandefreitas,atharwa-24,EmilStenstrom -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/samslow">
                    <img src="https://avatars1.githubusercontent.com/u/26738367?v=4" width="100;" alt="samslow"/>
                    <br />
                    <sub><b>Hyeonseok Samuel Seo</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/alandefreitas">
                    <img src="https://avatars0.githubusercontent.com/u/5369819?v=4" width="100;" alt="alandefreitas"/>
                    <br />
                    <sub><b>Alan De Freitas</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/atharwa-24">
                    <img src="https://avatars0.githubusercontent.com/u/54115798?v=4" width="100;" alt="atharwa-24"/>
                    <br />
                    <sub><b>Atharwa_24</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/emilstenstrom">
                    <img src="https://avatars.githubusercontent.com/u/224130?v=4" width="100;" alt="emilstenstrom"/>
                    <br />
                    <sub><b>Emil Stenström</b></sub>
                </a>
            </td>
		</tr>
	<tbody>
</table>
<!-- readme: samslow,alandefreitas,atharwa-24,EmilStenstrom -end -->

## Installation

#### Clone main repository or fork the project:

1. Build and activate the virtual environment:

   Make sure install Python first!

   ```bash
   python -m venv venv
   venv/Scripts/activate
   ```

2. Install dependencies requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. For generate images setting the OpenAI API key:

   Create an `.env` file in the same directory as the file using the OpenAI services for images generator and add `OPENAI_API_KEY=sk-xxxxxxxxxxxx...`

4. Huggingface Inference API:

   - In this project we add `free API Image Generator Model` from `Huggingface Inference API`access with our `Tokens`.
   - The `Tokens` working like `API keys`
   - Limit of number requests

     - If limit is full you can create `Tokens` using `Write` type in `Access Tokens` page from the `Huggingface Platform` and replace them in code file. example below

       ```bash
       InferenceClient("developers-name/models-name", token="hf_xxxxxx...")

       ```

## Start Web Application

Running on Streamlit Web Server:

```bash
streamlit run ui/ui.py

```

## Dependencies

```bash
groq # Text-to-Text
streamlit # Building Web Application using Python
pillow
openai # Text-to-Image
request
python-dotenv
huggingface_hub # Get the models from Huggingface

```

<h6 style="text-align:; color: grey;">A project from Artificial Intelligence Class</h6>
