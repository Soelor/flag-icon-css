{{
  forms.oauth_fields(
      'reCAPTCHA',
      (form.recaptcha_public_key, form.recaptcha_private_key),
      '''
        Domain name for <a href="https://www.google.com/recaptcha/admin" target="_blank">reCAPTCHA</a>:
        <em>%s</em>
      ''' % request.host
    )
}}
