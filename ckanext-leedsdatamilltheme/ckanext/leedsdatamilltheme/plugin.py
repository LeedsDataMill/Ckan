'''plugin.py

'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def wp_post(post_type, limit):
    from wordpress_xmlrpc import Client
    from wordpress_xmlrpc.methods import posts

    wp = Client('http://www.leedsdatamill.org/xmlrpc.php', 'USERNAME', 'PASSWORD')

    published_posts = wp.call(posts.GetPosts({'post_status': 'publish', 'number': limit, 'orderby': 'post_date', 'order': 'DESC', 'post_type': post_type }))
    return published_posts

def latest_datasets(limit=4):
    '''Return a list of the latest datasets on the site.'''
    response = toolkit.get_action('package_search')(
            data_dict={'sort': 'packages desc', 'rows': limit})
    return response['results']

def popular_datasets_recent(limit=1):
    '''Return a list of the most popular datasets on the site.'''
    response = toolkit.get_action('package_search')(
            data_dict={'sort': 'views_recent desc', 'rows': limit})
    return response['results']

def popular_datasets_alltime(limit=1):
    '''Return a list of the most popular datasets on the site.'''
    response = toolkit.get_action('package_search')(
            data_dict={'sort': 'views_count desc', 'rows': limit})
    return response['results']

def popular_users_alltime(limit=1):
    '''Return a list of the most popular users on the site.'''
    user = plugins.toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    user_list = plugins.toolkit.get_action('user_list')(context, {'sort': 'number_administered_packages'})
    filter_out = ['logged_in', 'visitor', 'default', 'admin']
    filtered_users_list = [u for u in user_list if u['name'] not in filter_out]
    return filtered_users_list[:limit]

def popular_users_recent(limit=1):
    '''Return a list of the most popular users on the site.'''
    user = plugins.toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    user_list = plugins.toolkit.get_action('user_list')(context, {'sort': 'number_administered_packages'})

    filter_out = ['logged_in', 'visitor', 'default', 'admin']
    filtered_users_list = [u for u in user_list if u['name'] not in filter_out]
    return filtered_users_list[:limit]
   # return user_list[:1]
   # return response['results']

def getTweets(hashtag, result_type, limit):
    from twython import Twython
    APP_KEY = 'APP_KEY'
    APP_SECRET = 'APP_SECRET'

    twitter = Twython(APP_KEY, APP_SECRET)
    results = twitter.search(q=hashtag, result_type=result_type, count=limit)

    return results

class LeedsDataMillThemePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')

         # Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        toolkit.add_public_directory(config, 'public')

    def get_helpers(self):

        '''Register the most_popular_groups() function above as a template
        helper function.
        '''

        return {
                'leedsdatamill_popular_datasets_alltime': popular_datasets_alltime,
                'leedsdatamill_popular_datasets_recent': popular_datasets_recent,
                'leedsdatamill_popular_users_alltime': popular_users_alltime,
                'leedsdatamill_popular_users_recent': popular_users_recent,
                'leedsdatamill_latest_datasets': latest_datasets,
                'leedsdatamill_tweets': getTweets,
                'leedsdatamill_wp': wp_post,
                }
