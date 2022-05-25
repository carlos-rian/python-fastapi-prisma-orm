from prisma.models import People

People.create_partial(name="PeoplePostAndPut", include={"name", "age"})
