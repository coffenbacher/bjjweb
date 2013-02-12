var lookup_node = function(uuid, nodes){
    var i = 0;
    for (n in nodes){
        if (nodes[n].uuid == uuid)
            return nodes[n];
        i++;
    }
}

var create_links = function(json){
    for (l in json.links){
        json.links[l].source = lookup_node(json.links[l].source, json.nodes);
        json.links[l].target = lookup_node(json.links[l].target, json.nodes);
    }
    return json;
}


var draw = function(d){
d = create_links(d);

/* Create graph data */
/* Create force graph */
var w = $("#view").width();
var h = $("#view").height();

var size = d.nodes.length;
d.nodes.forEach(function(d, i) { d.x = d.y = w / size * i});

svg = d3.select("#view")
            .append("svg:svg")
            .attr("width", w)
            .attr("weight", h)
            .attr("pointer-events", "all")
            .append('svg:g')
            .call(d3.behavior.zoom().on("zoom", redraw))
            .append('svg:g');

svg.append('svg:rect').attr('width', w).attr('height', h).attr('fill', 'white').attr('opacity', 0);


var force = d3.layout.force()
              .nodes(d.nodes)
              .links(d.links)
              .linkDistance(60)
              .charge(-900)
              .size([w, h]);

    var n = 800;
    force.start();
    for (var i = n * n; i > 0; --i) force.tick();
    force.stop();


// Per-type markers, as they don't inherit styles.
    var path = svg.append("svg:g").selectAll("path")
      .data(force.links())
      .enter().append("svg:path")
      .attr("class", function(d) { return "link " + d.type; })
    
    path.attr("d", function(d) {
        var dx = d.target.x - d.source.x,
        dy = d.target.y - d.source.y,
        dr = 0;
    return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
  });

    svg.append("svg:g")
       .selectAll("circle")
       .data(d.nodes)
       .enter().append("svg:ellipse")
       .attr("class", "node")
       .attr("fill", function(d) {return d.color})
       .attr("cx", function(d) { return d.x; })
       .attr("cy", function(d) { return d.y; })
       .attr("ry", 12)
       .attr("rx", 24);

    svg.append("svg:g")
       .selectAll("text")
       .data(d.nodes)
       .enter().append("svg:text")
       .attr("class", "flow-label")
       .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
       .attr("text-anchor", "middle")
       .attr("y", ".3em")
       .style("font-size", function(d){return (35 - d.name.length/1) / 4})
       .text(function(d) { return d.name; });
};

var redraw = function() {
  console.log("here", d3.event.translate, d3.event.scale);
  svg.attr("transform",
      "translate(" + d3.event.translate + ")"
      + " scale(" + d3.event.scale + ")");
}
