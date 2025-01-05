<h1 style="text-align: center;">Traveling Packages</h1>

## About the project

A web application for planning travel packages and creating image to promoting the province's landmark. This web application uses generative AI for creating travel packages (Text-to-Text) and image promoting (Text-to-Image).

## Contributors

<!-- readme: contributors -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/akhilmhdh">
                    <img src="https://avatars.githubusercontent.com/u/31166322?v=4" width="100;" alt="akhilmhdh"/>
                    <br />
                    <sub><b>Akhil Mohan</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/melroy89">
                    <img src="https://avatars.githubusercontent.com/u/628926?v=4" width="100;" alt="melroy89"/>
                    <br />
                    <sub><b>Melroy van den Berg</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/MrChocolatine">
                    <img src="https://avatars.githubusercontent.com/u/47531779?v=4" width="100;" alt="MrChocolatine"/>
                    <br />
                    <sub><b>Max Z</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/matks">
                    <img src="https://avatars.githubusercontent.com/u/3830050?v=4" width="100;" alt="matks"/>
                    <br />
                    <sub><b>Mathieu Ferment</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/athul">
                    <img src="https://avatars.githubusercontent.com/u/40897573?v=4" width="100;" alt="athul"/>
                    <br />
                    <sub><b>Athul Cyriac Ajay</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/dtcMLOps">
                    <img src="https://avatars.githubusercontent.com/u/115469901?v=4" width="100;" alt="dtcMLOps"/>
                    <br />
                    <sub><b>Daniel T</b></sub>
                </a>
            </td>
		</tr>
		<tr>
            <td align="center">
                <a href="https://github.com/jessebot">
                    <img src="https://avatars.githubusercontent.com/u/2389292?v=4" width="100;" alt="jessebot"/>
                    <br />
                    <sub><b>JesseBot</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/kachick">
                    <img src="https://avatars.githubusercontent.com/u/1180335?v=4" width="100;" alt="kachick"/>
                    <br />
                    <sub><b>Kenichi Kamiya</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/naomi-lgbt">
                    <img src="https://avatars.githubusercontent.com/u/63889819?v=4" width="100;" alt="naomi-lgbt"/>
                    <br />
                    <sub><b>Naomi Carrigan</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/KPCOFGS">
                    <img src="https://avatars.githubusercontent.com/u/100217654?v=4" width="100;" alt="KPCOFGS"/>
                    <br />
                    <sub><b>Shi Sheng</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/shufo">
                    <img src="https://avatars.githubusercontent.com/u/1641039?v=4" width="100;" alt="shufo"/>
                    <br />
                    <sub><b>Shuhei Hayashibara</b></sub>
                </a>
            </td>
		</tr>
	<tbody>
</table>
<!-- readme: contributors -end -->

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
