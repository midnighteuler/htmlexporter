import sys
import os

c_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(c_path)

import extractcsspreprocessor

c = get_config()
#`c.NbConvertApp.notebooks = sys.argv[1:]
c.NbConvertApp.export_format = 'html'
c.NbConvertApp.output_files_dir = 'output'

c.TemplateExporter.template_path = [c_path]
c.TemplateExporter.template_file = 'html_out.tpl'

c.Exporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor',
							'extractcsspreprocessor.ExtractCSSPreprocessor']

