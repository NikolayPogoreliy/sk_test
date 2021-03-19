import graphene

from backend.template.models import Chart
from backend.template.schema.types import ChartType


class CreateChart(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        metrics = graphene.List(graphene.ID)
        dimension = graphene.List(graphene.ID)
        pivot = graphene.List(graphene.ID)

    chart = graphene.Field(ChartType)

    def mutate(self, info, name, metrics: list, dimension: list, pivot: list = None):
        chart = Chart.objects.create(name=name)
        chart.metrics.set(metrics)
        chart.dimension.set(dimension)
        if pivot:
            chart.pivot.set(pivot)
        return CreateChart(chart=chart)


class UpdateChart(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        metrics = graphene.List(graphene.ID)
        dimension = graphene.List(graphene.ID)
        pivot = graphene.List(graphene.ID)

    chart = graphene.Field(ChartType)

    def mutate(self, info, id, **kwargs):
        name = kwargs.pop('name', None)

        chart = Chart.objects.filter(id=id)
        if chart.exists():
            if name:
                chart.update(name=name)

            for k in kwargs:
                field = getattr(chart.first(), k)
                field.set(kwargs.get(k))
        return UpdateChart(chart=chart.first())


class DeleteChart(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    chart = graphene.Field(ChartType)

    def mutate(self, info, id):
        chart = Chart.objects.filter(id=id)
        chart.delete()

        return DeleteChart(report=chart.first())


class ChartMutation:
    create_chart = CreateChart.Field()
    delete_chart = DeleteChart.Field()
    update_chart = UpdateChart.Field()
