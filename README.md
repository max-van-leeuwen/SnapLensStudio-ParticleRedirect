# SnapLensStudio-ParticleRedirect
A python script that generates data for Lens Studio's VFX Editor.
<br>It redirects particles to the bright areas in a black & white image! Useful for morphing particles between shapes, or spawn within a mask more efficiently.

<br/><br/>
  
![Particle Redirect morph](https://maxvanleeuwen.com/wp-content/uploads/morph.gif)


<br/><br/>
## When you would need this:

If you want particles to spawn within a texture, or if you want to store those positions in the particles' attributes so they can move from one to the next.

<br/><br/>
## What it does:

The Python script converts a square black & white image to a really small texture (<10kb), which contains all the positional information.
The custom Sub-Graph then reads the texture, and picks a position from it.
Its output can then be wired into the particle's world position, or it can be stored as an attribute for other uses.

<br/><br/>
## How to use it:

1. Run the Python script using 'python3 (this py path) (png path)', for example: 'python3 ./RedirectGenerator.py ./ExampleSpawnMap.png'.
2. A texture file of the same name with '\_redirect' appended will appear in the same folder. This can be imported into your Lens Studio resources panel.
3. Then, import the 'particle redirect.subgraph' file into your VFX Editor panel and connect a 'Texture 2D Object Parameter' to it.

See the included example Lens Studio project!
