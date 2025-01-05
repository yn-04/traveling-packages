<h1 style="text-align: center;">Traveling Packages</h1>

## About the project

A web application for planning travel packages and creating image to promoting the province's landmark. This web application uses generative AI for creating travel packages (Text-to-Text) and image promoting (Text-to-Image).

## Collaborators

<!-- readme: collaborators -start -->
<!-- readme: collaborators -end -->

## Contributors

<!-- readme: contributors -start -->

# <!-- readme: contributors -end -->

<!-- readme: collaborators,contributors -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/modpanyakorn">
                    <img src="https://avatars.githubusercontent.com/u/68369082?v=4" width="100;" alt="modpanyakorn"/>
                    <br />
                    <sub><b>Panyakorn Timchanthuek</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/gittium">
                    <img src="https://avatars.githubusercontent.com/u/157870955?v=4" width="100;" alt="gittium"/>
                    <br />
                    <sub><b>gittium</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/bbtpm">
                    <img src="https://avatars.githubusercontent.com/u/135986939?v=4" width="100;" alt="bbtpm"/>
                    <br />
                    <sub><b>bbtpm</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/yn-04">
                    <img src="https://avatars.githubusercontent.com/u/186150397?v=4" width="100;" alt="yn-04"/>
                    <br />
                    <sub><b>yn-04</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/JaoBen">
                    <img src="https://avatars.githubusercontent.com/u/180035510?v=4" width="100;" alt="JaoBen"/>
                    <br />
                    <sub><b>JaoBen</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/rarossaa">
                    <img src="https://avatars.githubusercontent.com/u/180069307?v=4" width="100;" alt="rarossaa"/>
                    <br />
                    <sub><b>rossaa</b></sub>
                </a>
            </td>
		</tr>
	<tbody>
</table>
<!-- readme: collaborators,contributors -end -->
>>>>>>> bca65a54d6798a21737074f808ea7ff56271687e

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
