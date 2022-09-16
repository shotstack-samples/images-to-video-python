# Turn Images To Slideshow Videos Using Python & Shotstack API

This Python program turns images to slideshow videos with music using Python, [Shotstack Python SDK](https://pypi.org/project/shotstack-sdk/0.2.1/), and Shotstack API. See [this tutorial](https://shotstack.io/learn/turn-images-to-slideshow-video-using-python/?utm_source=github&utm_campaign=demo_repos) to learn how it works.


### What is Shotstack API?

Shotstack API is a cloud based video editing API that enables you to render multiple videos concurrently in the cloud using your favourite programming language. Sign up for a free developer account [here](https://dashboard.shotstack.io/register?utm_source=github&utm_campaign=demo_repos) to get your API key. 

### Why use Shotstack API?

Rendering videos is a resource consuming process. It may take several minutes to render one video depending on the complexity of the video. Shotstack enables to concurrently render multiple videos in the powerful cloud infrastructure. This reduces rendering time and fastens the process. Visit our [Docs](https://shotstack.io/docs/guide/getting-started/core-concepts/?utm_source=github&utm_campaign=demo_repos) to learn more.

Checkout other Python demo examples in this [Github repo](https://github.com/shotstack/python-demos).


### Installation

Clone this repository with following command

```bash
git clone https://github.com/shotstack-samples/images-to-videos-Python.git
```

Go inside the project directory
```bash
cd images-to-video-python
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

### Final video example

Here is what the final rendered video looks like:
<video id="player" playsinline controls>
  <source src="https://cdn.shotstack.io/au/stage/c9npc4w5c4/a4199fa0-d65c-42f2-aa5c-c5722fb48886.mp4" type="video/mp4" />
</video>

### Accessing rendered videos

To access your rendered videos, sign into your Shotstack account. Inside the dashboard, you can find all rendered videos under Renders tab.

![Alt Text](https://im5.ezgif.com/tmp/ezgif-5-9da1b35692.gif)


### Edit and automate video production using Python

This is just a basic example. You can do more with Shotstack Python SDK and API like: 
- Beautify videos by adding effects, transitions, overlays, titles
- Automate video editing and production
- Personalize videos with code
- Convert media files i.e. gif, mp3, mp4, jpg, bmp, and png
- Generate, add SRT files to multiple videos concurrently
- Use AI to generate media assets to produce videos

See our other [tutorial articles](https://shotstack.io/learn/?utm_source=github&utm_campaign=demo_repos) to learn video editing using Python. 