import os



with open("./index.html", 'r') as web:
	content = str(web.read()).split('<div class="row portfolio-container" data-aos="fade-up">')




def add_():
	name = str(input("Enter the name here\n"))
	link = str(input("Link here\n"))
	img_src = str(input("img_src here\n"))
	type1 = str(input("type here\n")).lower()
	if type1 == 'article':
		type1 = 'app'
	elif type1 == 'research paper':
		type1 = 'card'
	elif type1 == 'readings':
		type1 = 'web'

	add = '<div class="row portfolio-container" data-aos="fade-up">\n\n          <div class="col-lg-4 col-md-6 portfolio-item filter-{}">\n            <div class="portfolio-wrap">\n             <img src="{}" class="img-fluid" alt="">\n              <div class="portfolio-links">\n                <a target="_blank" href="{}" data-gallery="portfolioGallery" class="portfolio-lightbox">{}</i></a>\n                <a target="_blank" href="{}" title="View Paper.."><i class="bx bx-link"></i></a>\n              </div>\n            </div>\n          </div>'.format(type1, img_src, img_src, name, link)
	with open("./index.html", 'w') as file:
		file.write(str('{}{}{}'.format(content[0], add, content[1])))



add_()

