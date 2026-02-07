from flask import Flask, render_template, request
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Ensure Flask knows where to find templates/static when running from api/ (e.g. Vercel)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
template_dir = os.path.join(project_root, 'templates')
static_dir = os.path.join(project_root, 'static')
# Ensure Flask's static URL path matches where Vercel will serve static files
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, static_url_path='/static')

reuse_suggestions = {
    'plastic': [
        ("Plastic bottles can be used as planters.", "https://www.instructables.com/Plastic-Bottle-Planters/", "Create beautiful planters from plastic bottles."),
        ("Use plastic bags to store items.", "https://www.diycraftsy.com/how-to-store-plastic-bags/", "Learn creative ways to store items using plastic bags."),
        ("Repurpose plastic containers for organizing small items.", "https://www.almostzerowaste.com/repurposing-plastic-ideas/", "Plastic containers can help with organizing small objects."),
        ("Create a bird feeder using a plastic bottle.", "https://www.wikihow.com/Make-a-Bird-Feeder-with-a-Plastic-Bottle", "Make a simple bird feeder out of a plastic bottle."),
        ("Turn plastic bottles into art crafts.", "https://bottlefirst.com/plastic-bottle-crafts-simple/", "Repurpose plastic for fun and creative art projects."),
        ("Use plastic to make homemade ice packs.", "https://www.wikihow.com/Make-a-Homemade-Ice-Pack", "Turn plastic into DIY ice packs for the home."),
        ("Repurpose plastic bottles to create a vertical garden.", "https://balconygardenweb.com/plastic-bottle-vertical-garden-soda-bottle-garden/", "Plastic bottles can help you create a vertical garden."),
    ],
    'paper': [
        ("Make DIY crafts with old newspapers.", "https://craftingagreenworld.com/articles/30-awesome-diy-projects-using-newspaper/", "Repurpose newspapers into fun and creative DIY projects."),
        ("Use paper to create scrapbooks.", "https://www.thesprucecrafts.com/making-a-basic-scrapbook-page-4121913", "Create beautiful scrapbooks with your old paper."),
        ("Turn paper into handmade greeting cards.", "https://www.simonstapleton.com/upcycle-greetings-cards/", "Craft greeting cards from paper."),
        ("Create paper flowers for decorations.", "https://thecraftyblogstalker.com/how-to-make-20-different-paper-flowers/", "Make stunning paper flowers for home decor."),
        ("Use old newspapers for gift wrapping.", "https://thegoodoldways.substack.com/p/how-to-wrap-gifts-the-old-fashioned", "Use paper for eco-friendly gift wrapping."),
        ("Repurpose paper for DIY wall art.", "https://www.homeaswemakeit.com/17-diy-wall-art-ideas-using-recycled-paper-products/", "Transform paper into unique wall art."),
    ],
    'metal': [
        ("Turn metal cans into organizers.", "https://www.craftionary.net/recycling-tin-cans-into-organizers-tutorial/", "Repurpose tin cans into useful organizers."),
        ("Repurpose metal tins for kitchen storage.", "https://www.instructables.com/Upcycle-metal-food-tins-into-storage-containers/", "Repurpose metal tins for kitchen storage."),
        ("Turn metal cans into bird feeders.", "https://www.instructables.com/Recycled-Can-Bird-Feeder/", "Create bird feeders using metal cans."),
        ("Use metal bottle caps for decorative art.", "https://wonderfuldiy.com/diy-bottle-cap-craft-ideas/", "Transform metal bottle caps into art."),
        ("Repurpose metal pipes for unique furniture.", "https://www.journeymanhq.com/21919/creative-ways-to-use-reclaimed-pipes/", "Create unique furniture from metal pipes."),
        ("Make a metal lantern from a soda can.", "https://www.instructables.com/Hand-Lantern-From-Soda-Cans/", "Craft beautiful metal lanterns from soda cans."),
    ],
    'glass': [
        ("Make candle holders out of glass bottles.", "https://www.instructables.com/Make-a-Candle-Holder-From-a-Glass-Bottle/", "Turn glass bottles into charming candle holders."),
        ("Turn glass jars into storage containers.", "https://earthysapo.com/blogs/news/10-creative-ways-to-repurpose-glass-for-a-more-sustainable-lifestyle", "Glass jars can be used for organizing items."),
        ("Create a glass bottle chandelier.", "https://www.instructables.com/Rustic-Glass-Bottle-Chandelier/", "Create an elegant chandelier with glass bottles."),
        ("Repurpose glass bottles as herb planters.", "https://bloomyheaven.com/garden-ideas-using-recycled-glass-bottles/", "Use glass bottles as herb planters."),
        ("Create mosaics with broken glass pieces.", "https://1millionideas.com/upcycled-mosaic-tile-ideas", "Make mosaics from broken glass pieces."),
        ("Make a terrarium in a glass bottle.", "https://terrariumtribe.com/terrarium-bottle-garden/", "Create a beautiful terrarium inside a glass bottle."),
    ],
    'organic': [
        ("Compost organic waste.", "https://green.org/2024/01/30/composting-a-sustainable-way-to-manage-organic-waste/", "Learn how to compost organic waste at home."),
        ("Create organic fertilizers for plants.", "https://www.almanac.com/how-make-organic-plant-fertilizer-home", "Make your own organic fertilizers."),
        ("Create mulch for gardens from organic matter.", "https://completegardening.com/15-organic-mulching-materials-that-will-transform-your-garden-beds/", "Turn organic waste into mulch for gardens."),
        ("Repurpose coffee grounds for plant fertilization.", "https://plantisima.com/ways-to-use-coffee-grounds-in-the-garden-that-actually-work/", "Use coffee grounds to fertilize plants."),
        ("Use banana peels to enrich the soil.", "https://whatisgreenliving.com/how-to-use-dried-banana-peel-as-fertilizer/", "Banana peels can help enrich your garden soil."),
        ("Make DIY organic pest repellents.", "https://www.agrifarming.in/how-to-make-homemade-pesticides-15-diy-recipes", "Create natural pest repellents using organic materials."),
        ("Create worm composting bins.", "https://www.wikihow.com/Make-a-Worm-Compost-System", "Learn how to set up a worm composting bin for organic waste."),
    ]
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/suggestions', methods=['POST'])
def suggestions():
    if request.method == 'POST':
        waste_type = request.form['waste_type']
        suggestions = reuse_suggestions.get(waste_type, [])
        return render_template('suggestions.html', suggestions=suggestions, waste_type=waste_type)


if __name__ == '__main__':
    app.run(debug=True)
