


from html2image import Html2Image
hti = Html2Image(browser= 'chrome',output_path= '/u/shahhi/vccf_computations_data/image_vccf_placenta', size = (1920,1080))

paths = hti.screenshot(
    html_file='Image.html',
    save_as='blue_page.png'
)

print(paths)