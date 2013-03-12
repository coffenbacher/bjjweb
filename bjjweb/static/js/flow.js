var draw = function(d){
    initialize_svg();
    var force = initialize_force(d);
    render_links(d.nodes, force);
    render_nodes(d.nodes);
}

var redraw = function() {
  d3.select("#base").attr("transform",
      "translate(" + d3.event.translate + ")"
      + " scale(" + d3.event.scale + ")");
}

var initialize_force = function(d){
    d = create_links(d);
    
    var w = $("#view").width();
    var h = $("#view").height();

    var force = d3.layout.force()
                  .nodes(d.nodes)
                  .links(d.links)
                  .linkDistance(80)
                  .charge(-900)
                  .size([w, h]);
    
    var n = 800;
    force.start();
    for (var i = n * n; i > 0; --i) force.tick();
    force.stop();
    return force;
}

var initialize_svg = function(){
    var base = d3.select("#view")
        .append("svg:svg")
        .attr("pointer-events", "all")
        .call(d3.behavior.zoom().on("zoom", redraw))
        .append("svg:g")
        .attr("id", "base")
        ;

    // scale view
    base.append('svg:rect')
        .attr("id", "bg")
        .attr("width", $("#view").width())
        .attr("height", $("#view").height())
        .attr('opacity', 0);
}

var render_nodes = function(nodes){
    var base = d3.select("#base");
    var RADIUS = 24;
    base.append("svg:g")
       .attr("id", "nodes")
       .selectAll("circle")
       .data(nodes)
       .enter().append("svg:ellipse")
       .attr("class", "node")
       .attr("fill", function(d) {return d.color})
       .attr("cx", function(d) { return d.x; })
       .attr("cy", function(d) { return d.y; })
       .attr("ry", RADIUS / 1.618)
       .attr("rx", RADIUS)
       .on("click", function(d) { window.open(d.url, '_blank')});
    
    base.append("svg:g")
       .attr("id", "text")
       .selectAll("text")
       .data(nodes)
       .enter().append("svg:text")
       .attr("class", "flow-label")
       .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
       .attr("text-anchor", "middle")
       .attr("y", ".3em")
       .style("font-size", function(d){return (35 - d.name.length/1) / 4})
       .text(function(d) { return d.name; })
       .on("click", function(d) { window.open(d.url, '_blank')});
};

var render_links = function(d, force){
    var ARROW_COLOR = "black";
    var base = d3.select("#base");
    var path = base.append("svg:g").selectAll("path")
      .data(force.links())
      .enter().append("svg:path")
      .attr("class", function(d) { return "link " + d.type; })
    
    path.attr("id", function(d){
        return d.source.uuid + d.target.uuid;
    });

    path.attr("d", function(d) {
        var dx = d.target.x - d.source.x,
        dy = d.target.y - d.source.y,
        dr = Math.sqrt(dx * dx + dy * dy);
        return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
      });


    base.selectAll("path").each(function(d,i){
        var thing = base.append("svg:g")
            .attr("id", "thing")
            .style("fill", ARROW_COLOR);

        thing.append("text")
            .style("font-size", "0.5em")
            .attr("dy", "0.3em")
          .append("textPath")
            .attr("xlink:href", "#"+this.id)
            .text(Array(100).join(" > - "));

        thing.append("use")
            .attr("xlink:href", "#"+this.id)
        .style("stroke", "black")
    });
}


var create_links = function(j){
    var complete_links = [];
    for (l in j.links){
        var source = lookup_node(j.links[l].source, j.nodes);
        var target = lookup_node(j.links[l].target, j.nodes);
        if (source && target) {
            var link = j.links[l];
            link.source = source;
            link.target = target;
            complete_links.push(link);
        }
    }
    j.links = complete_links;
    return j;
}

var lookup_node = function(pk, nodes){
    var i = 0;
    for (n in nodes){
        if (nodes[n].pk == pk)
            return nodes[n];
        i++;
    }
}
