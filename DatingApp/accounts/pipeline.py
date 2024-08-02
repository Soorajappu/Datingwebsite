def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        user.email = response.get('email')
        user.save()
