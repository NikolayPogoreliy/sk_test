import graphene
from graphql_relay import from_global_id

from backend.template.models import Chart, Dimension, Metric, Pivot, Template
from backend.template.schema.types import ChartType, DimensionType, MetricType, PivotType, TemplateType


class CreateChart(graphene.Mutation):
    """ Mutation for chart creation """
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
    """ Mutation for chart updating
    can change name, add pivots, metrics and dimensions
    """

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
    """ Delete chart """
    class Arguments:
        id = graphene.ID()

    chart = graphene.Field(ChartType)

    def mutate(self, info, id):
        chart = Chart.objects.filter(id=id)
        chart.delete()

        return DeleteChart(chart=chart.first())


class ChartMutation:
    create_chart = CreateChart.Field()
    delete_chart = DeleteChart.Field()
    update_chart = UpdateChart.Field()


class CreatePivot(graphene.Mutation):
    """ Create pivot """
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
    """ Update pivot """
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
    """ Delete Pivot"""
    class Arguments:
        id = graphene.ID()

    pivot = graphene.Field(ChartType)

    def mutate(self, info, id):
        pivot = Pivot.objects.filter(id=id)
        pivot.delete()

        return DeletePivot(pivot=pivot.first())


class PivotMutation:
    create_pivot = CreatePivot.Field()
    delete_pivot = DeletePivot.Field()
    update_pivot = UpdatePivot.Field()


class CreateDimension(graphene.Mutation):
    """ Add GA dimension """
    class Arguments:
        name = graphene.String()

    dimension = graphene.Field(DimensionType)

    def mutate(self, info, name):
        dimension = Dimension.objects.create(name=name)
        return CreateDimension(dimension=dimension)


class UpdateDimension(graphene.Mutation):
    """ Update GA dimension name """
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
    """ Delete GA dimension"""
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
    """ Create GA metric """
    class Arguments:
        name = graphene.String()

    metric = graphene.Field(MetricType)

    def mutate(self, info, name):
        metric = Metric.objects.create(name=name)
        return CreateMetric(metric=metric)


class UpdateMetric(graphene.Mutation):
    """ Update GA metric name """
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
    """ Delete GA metric """
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


class CreateTemplate(graphene.Mutation):
    """ Create template:
    contains:
        name
        GA viewId
        charts
        filter expression (common for all charts in template)
    """

    class Arguments:
        name = graphene.String()
        charts = graphene.List(graphene.ID)
        ga_view_id = graphene.String()
        filter_expression = graphene.String()

    template = graphene.Field(TemplateType)

    def mutate(self, info, name, charts: list, ga_view_id: int, filter_expression: str = None):
        template = Template.objects.create(name=name, ga_view_id=ga_view_id, filter_expression=filter_expression)
        template.charts.set(charts)
        return CreateTemplate(template=template)


class UpdateTemplate(graphene.Mutation):
    """
        Update template
            name
            charts
            GA viewId
            filter expression
    """

    class Arguments:
        id = graphene.String()
        name = graphene.String()
        charts = graphene.List(graphene.ID)
        ga_view_id = graphene.String()
        filter_expression = graphene.String()

    template = graphene.Field(TemplateType)

    def mutate(self, info, id, **kwargs):
        charts = kwargs.pop('charts', None)

        template = Template.objects.filter(id=from_global_id(id)[1])
        if template.exists():
            template.update(**kwargs)

            if charts:
                template.charts.set(charts)
        return UpdateTemplate(template=template.first())


class DeleteTemplate(graphene.Mutation):
    """ Delete template """
    class Arguments:
        id = graphene.String()

    template = graphene.Field(ChartType)

    def mutate(self, info, id):
        chart = Template.objects.filter(id=from_global_id(id)[1])
        chart.delete()

        return DeleteChart(template=chart.first())


class TemplateMutation:
    create_template = CreateTemplate.Field()
    delete_template = DeleteTemplate.Field()
    update_template = UpdateTemplate.Field()
