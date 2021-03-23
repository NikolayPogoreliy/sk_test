import graphene

from backend.template.models import Chart, Dimension, Metric, Pivot
from backend.template.schema.types import ChartType, DimensionType, MetricType, PivotType


class CreateChart(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        metrics = graphene.List(graphene.ID)
        dimensions = graphene.List(graphene.ID)
        pivot = graphene.List(graphene.ID)

    chart = graphene.Field(ChartType)

    def mutate(self, info, name, metrics: list, dimensions: list, pivots: list = None):
        chart = Chart.objects.create(name=name)
        chart.metrics.set(metrics)
        chart.dimensions.set(dimensions)
        if pivots:
            chart.pivots.set(pivots)
        return CreateChart(chart=chart)


class UpdateChart(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        metrics = graphene.List(graphene.ID)
        dimensions = graphene.List(graphene.ID)
        pivots = graphene.List(graphene.ID)

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


class CreatePivot(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        metrics = graphene.List(graphene.ID)
        dimensions = graphene.List(graphene.ID)
        max_group_count = graphene.Int()
        start_group = graphene.Int()

    pivot = graphene.Field(PivotType)

    def mutate(self, info, name, metrics: list, dimensions: list, max_group_count: int, start_group: int):
        pivot = Pivot.objects.create(name=name, max_group_count=max_group_count, start_group=start_group)
        pivot.metrics.set(metrics)
        pivot.dimensions.set(dimensions)
        return CreatePivot(pivot=pivot)


class UpdatePivot(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        metrics = graphene.List(graphene.ID)
        dimensions = graphene.List(graphene.ID)
        max_group_count = graphene.Int()
        start_group = graphene.Int()

    pivot = graphene.Field(PivotType)

    def mutate(self, info, id, **kwargs):
        pivot = Pivot.objects.filter(id=id)
        if pivot.exists():
            name = kwargs.pop('name', None)
            if name:
                pivot.update(name=name)
            for k in kwargs:
                field = getattr(pivot.first(), k)
                field.set(kwargs.get(k))
        return UpdatePivot(pivot=pivot.first())


class DeletePivot(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    pivot = graphene.Field(ChartType)

    def mutate(self, info, id):
        pivot = Pivot.objects.filter(id=id)
        pivot.delete()

        return DeletePivot(report=pivot.first())


class PivotMutation:
    create_pivot = CreatePivot.Field()
    delete_pivot = DeletePivot.Field()
    update_pivot = UpdatePivot.Field()


class CreateDimension(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    dimension = graphene.Field(DimensionType)

    def mutate(self, info, name, metrics: list, dimensions: list, max_group_count: int, start_group: int):
        dimension = Dimension.objects.create(name=name)
        return CreateDimension(dimension=dimension)


class UpdateDimension(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    dimension = graphene.Field(DimensionType)

    def mutate(self, info, id, **kwargs):
        dimension = Dimension.objects.filter(id=id)
        if dimension.exists():
            if 'name' in kwargs:
                dimension.update(name=kwargs.get('name'))
        return UpdateDimension(dimension=dimension.first())


class DeleteDimension(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    dimension = graphene.Field(DimensionType)

    def mutate(self, info, id):
        dimension = Dimension.objects.filter(id=id)
        dimension.delete()

        return DeleteDimension(dimension=dimension.first())


class DimensionMutation:
    create_dimension = CreateDimension.Field()
    delete_dimension = DeleteDimension.Field()
    update_dimension = UpdateDimension.Field()


class CreateMetric(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    metric = graphene.Field(MetricType)

    def mutate(self, info, name, metrics: list, dimensions: list, max_group_count: int, start_group: int):
        metric = Metric.objects.create(name=name)
        return CreateMetric(metric=metric)


class UpdateMetric(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    metric = graphene.Field(MetricType)

    def mutate(self, info, id, **kwargs):
        metric = Metric.objects.filter(id=id)
        if metric.exists() and 'name' in kwargs:
            metric.update(name=kwargs.get('name'))
        return UpdateMetric(metric=metric.first())


class DeleteMetric(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    metric = graphene.Field(DimensionType)

    def mutate(self, info, id):
        metric = Metric.objects.filter(id=id)
        metric.delete()

        return DeleteMetric(metric=metric.first())


class MetricMutation:
    create_metric = CreateMetric.Field()
    delete_metric = DeleteMetric.Field()
    update_metric = UpdateMetric.Field()
