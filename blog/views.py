from django.shortcuts import render, get_object_or_404
from blog import models
from django.core.paginator import Paginator
from django.conf import settings

# 博客详情
def blog_detail(request, blog_id):
    context = {}
    context['blog'] = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'blog_detail.html', context)


# 博客列表
def blog_list(request):
    blog_all_list = models.Blog.objects.all()
    paginator = Paginator(blog_all_list, settings.PAGE_DATA_SIZE) # 从 settings 里读取每页显示多少条数据
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)

    # 获取当前页码
    current_page_num = page_of_blogs.number

    # 获取当前页的前两页和后两页范围
    page_range = list(range(max(current_page_num-2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages)+1))

    # 增加省略符号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >=2:
        page_range.append('...')

    # 增加首尾页码
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['page_range'] = page_range
    context['page_ob_blogs'] = page_of_blogs
    return render(request, 'blog_list.html', context)
