import plotly.express as px
from utils import def_rec_estado,def_rec_mesal,def_rec_categoria,def_vendedor

grafico_map_estado = px.scatter_geo(
 def_rec_estado,
  lat="lat",
  lon="lon",
  scope="south america",
  size="Preco",
  template="seaborn",
  hover_name="Local_da_compra",
  hover_data={"lat" : False, "lon" : False},
  title="Receita por Estado"
  
)
grafico_rec_mensal = px.line(
 def_rec_mesal,
 x="Mes",
 y="Preco",
 markers=True,
 range_y=(0,def_rec_mesal.max()),
 color="Ano",
 line_dash="Ano",
 title="Receita Mensal",
)

grafico_rec_mensal.update_layout(yaxis_title="Receita")

grafico_rec_estado = px.bar(
 def_rec_estado.head(5),
 x="Local_da_compra",
 y="Preco",
 color="Local_da_compra",
 template="seaborn",
 title="Receita por Estado"
)

grafico_rec_estado.update_layout(yaxis_title="Receita")

grafico_rec_categoria = px.bar(
 def_rec_categoria.head(5),
 text_auto=True,
 title="Top 5 Categorias com Maior Receita"
)
grafico_rec_vendedores = px.bar(
 def_vendedor[["sum"]].sort_values("sum",ascending=False).head(5),
 x="sum",
 y=def_vendedor[["sum"]].sort_values("sum",ascending=False).index,
 text_auto=True,
 title="Top 5 Vendedores com Maior Receita"

)
grafico_vendas_vendedores = px.bar(
 def_vendedor[["count"]].sort_values("count",ascending=False).head(5),
 x="count",
 y=def_vendedor[["count"]].sort_values("count",ascending=False).index,
 text_auto=True,
 title="Top 5 Vendedores com Maior Vendas"
)