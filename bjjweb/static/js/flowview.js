$(document).ready(function(){
    vis = d3.select("#view")
      .append("svg:svg")
        .attr("width", w)
        .attr("height", h)
        .attr("pointer-events", "all")
      .append('svg:g')
        .call(d3.behavior.zoom().on("zoom", redraw))
      .append('svg:g');

    vis.append('svg:rect')
        .attr('width', w)
        .attr('height', h)
        .attr('fill', 'white');
});

