## Turn Images To Slideshow Videos Using Python & Shotstack API

This mini Python program turns images to slideshow videos with music using Python, Shotstack Python SDK, and Shotstack API. Checkout [this tutorial](https://shotstack.io/learn/turn-images-to-slideshow-video-using-python/?utm_source=github&utm_campaign=demo_repos) to learn how it works.


### What is Shotstack API?

Shotstack API is a cloud based video editing API that enables you to render multiple videos concurrently in the cloud using your favourite programming language. Sign up for a free developer account [here](https://dashboard.shotstack.io/register?utm_source=github&utm_campaign=demo_repos) to get your API key. 

### Why Shotstack API?

Rendering videos is a resource consuming process. It may take several minutes to render one video depending on the attributes of the video. Shotstack enables to concurrently render multiple videos in the powerful cloud infrastructure. This reduces rendering time and fastens the process. See Docs [here](https://shotstack.io/docs/guide/getting-started/core-concepts/?utm_source=github&utm_campaign=demo_repos) to learn more. 


### Installation

```bash
git clone https://github.com/shotstack-samples/images-to-videos-Python.git
```

```bash
cd images-to-video-python-Shotstack-API
```

Install the required dependencies including the [Shotstack Python SDK](https://pypi.org/project/shotstack-sdk/0.2.1/)

```bash
pip3 install -r requirements.txt
```


### Set your API key

The demos use the **staging** endpoint by default so use your provided **staging** key:

```bash
export SHOTSTACK_KEY=your_key_here
```

Windows users (Command Prompt):

```bash
set SHOTSTACK_KEY=your_key_here
```

You can [get an API key](http://shotstack.io/register?utm_source=github&utm_campaign=demo_repos) by signing up for a free developer account via the Shotstack web site.


### Running the program

To run this program, run the `main.py` inside the root folder:

```bash
python images-to-videos-Python/main.py
```

### Accessing rendered videos

To access your rendered videos, sign into your Shotstack account. Inside the dashboard, you can find all rendered videos under Renders tab.

![Alt Text](https://im5.ezgif.com/tmp/ezgif-5-9da1b35692.gif)


### Edit and automate video production using Python

This is just a basic example. You can do more with Shotstack Python SDK and API like 
- Beautify video by adding effects, transitions, overlays, titles
- Automate video editing and production
- Personalize videos with code
- Convert media files to gif, mp3
- Generate, add transcripts to multiple videos concurrently
- Use AI to generate media assets to produce videos

See our other [tutorial articles](https://shotstack.io/learn/?utm_source=github&utm_campaign=demo_repos) to learn video editing using Python. 