from django.template.defaultfilters import slugify

def create_slug(sender, instance, signal, *args, **kwargs):
    # Verifica o id e atributos
    if instance.id and hasattr(instance, 'slug_field_name') and hasattr(instance, 'slug_from'):
        # Pega as informações do slug field
        slug_name = instance.slug_field_name
        slug_from = instance.slug_from
        # Se não existir valor no slug, ele cria um.
        if not getattr(instance, slug_name, None):
            #Cria slug
            slug = '%s-' % instance.id + slugify(getattr(instance, slug_from))
            setattr(instance, slug_name, slug)
            instance.save()