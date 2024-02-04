# tabletop-image-hints
These are python scripts I wrote to create hidden hints to players when running a tabletop game. The first script [create_key.py](/src/scripts/create_key.py) will create the keys for each of the colors and the [generate_cypher.py](/src/scripts/generate_cypher.py) script will create the background image that includes all of the image cyphers that can be "unlocked" with the keys.

## Creation of image files
1. You'll need 3 image files which contain hints for the players. The images should be binary (black/white) in order to provide the best contrast.
2. Create the keys by running the create_key.py script:

```python create_key.py```

3. Create the cypher image by running the generater_cypher.py script, using the keys and images as input:

```python generate_cipher.py "red.png,green.png,blue.png" "key_red.png,key_green.png,key_blue.png"```

## Images
The keys can be overlayed ontop of the cypher image to show the hidden values. For example, [key_red](/example_images/key_red.png):
![key_red.png](/example_images/key_red.png)
Can be overlayed onto the [CypherImage](/example_images/CypherImage.png):
![CypherImage](/example_images/CypherImage.png)
To show the hidden message:
![combined_red_image.png](/example_images/combined_red_image.png)
