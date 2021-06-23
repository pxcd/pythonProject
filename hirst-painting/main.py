import colorgram
# from PIL import Image


colors = colorgram.extract('image.jpg', 10)

# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
#
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s