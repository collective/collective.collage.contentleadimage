from Products.Collage.browser.views import BaseView
from collective.contentleadimage.browser.folder_leadimage_view import FolderLeadImageView

class ContentLeadImageCollageView(BaseView, FolderLeadImageView):
    title = u'Summary (lead images)'
