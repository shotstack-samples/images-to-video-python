import shotstack_sdk as shotstack
import os
import sys

from shotstack_sdk.model.soundtrack  import Soundtrack
from shotstack_sdk.api               import edit_api
from shotstack_sdk.model.clip        import Clip
from shotstack_sdk.model.track       import Track
from shotstack_sdk.model.timeline    import Timeline
from shotstack_sdk.model.output      import Output
from shotstack_sdk.model.edit        import Edit
from shotstack_sdk.model.merge_field import MergeField
from shotstack_sdk.model.title_asset import TitleAsset

if __name__ == "__main__":
    host = "https://api.shotstack.io/stage"

    if os.getenv("SHOTSTACK_HOST") is not None:
        host =  os.getenv("SHOTSTACK_HOST")

    configuration = shotstack.Configuration(host = host)

    #Make sure you have set your API key as an environment variable
    if os.getenv("SHOTSTACK_KEY") is None:
        sys.exit("API Key is required. Set using: export SHOTSTACK_KEY=your_key_here")  

    configuration.api_key['DeveloperKey'] = os.getenv("SHOTSTACK_KEY")

    with shotstack.ApiClient(configuration) as api_client:
        api_instance = edit_api.EditApi(api_client)

        # You may replace the image URLs with your own
        images = [
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-712850.jpeg",
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-867452.jpeg",
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-752036.jpeg",
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-572487.jpeg",
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-114977.jpeg",
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-347143.jpeg",
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-206290.jpeg",
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-940301.jpeg",
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-266583.jpeg",
            "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/examples/images/pexels/pexels-photo-539432.jpeg"
        ]

        # You may replace the soundtrack URL with your own
        soundtrack = Soundtrack(
            src     = "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/music/disco.mp3",
            effect  = "fadeInFadeOut"
        )


        title_asset = TitleAsset(
            style = "minimal",
            text  = "Hello {{NAME}}",
            size  = "x-small"
        )

        title = Clip(
            asset  = title_asset,
            start  = 0.0,
            length = 5.0,
            effect = "zoomIn"
        )

        track = Track(clips = [title])

        timeline = Timeline(
            background = "#000000",
            soundtrack = soundtrack,
            tracks     = [track]
        )

        output = Output(
            format      = "mp4",
            resolution  = "sd"
        )

        merge_field = MergeField(
            find    = "NAME",
            replace = "Jane"
        )

        edit = Edit(
            timeline = timeline,
            output   = output,
            merge    = [merge_field]
        )

        try:
            api_response = api_instance.post_render(edit)

            message = api_response['response']['message']
            id = api_response['response']['id']
        
            print(f"{message}\n")
            print(">> Now check the progress of your render by running:")
            print(f">> python examples/status.py {id}")
        except Exception as e:
            print(f"Unable to resolve API call: {e}")