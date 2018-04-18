created_at = datetime.strptime(
        image.creation_date,
        "%Y-%m-%dT%H:%M:%S.000Z",
        )

    if created_at > datetime.now() - timedelta(days=50):