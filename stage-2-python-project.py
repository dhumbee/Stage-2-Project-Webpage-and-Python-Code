def make_notes(subheadingbox, box_description):
	html_1='''
	  <div class="subheadingbox">
	  	<h4>
	  		'''+subheadingbox
	html_2='''
		</h4>
			<div class="box_description">
				<p>
					'''+box_description
	html_3='''
				</p>
			</div>
	  </div>'''

	full_html=html_1+html_2+html_3
	return full_html


def make_html(lesson):
	subheadingbox=lesson[0]
	box_description=lesson[1]
	return make_notes(subheadingbox, box_description)

full_lesson=[["The Web", "The web is a collection of HTML documents."],
			["Using and Making Procedures", "Procedures are a way to package code so it can be reused."], 
			["Mutation", "Lists support Mutation, meaning we can change a value in a list after it's created."]]

def all_html(many_lessons):
	HTML=""
	for lesson in many_lessons:
		lesson_html=make_html(lesson)
		HTML=HTML+lesson_html
	return HTML

print all_html(full_lesson)