$(document).ready(function(){


	var popup_limit = 3;


	$('#start').click(function(){

		var i = 0;	
		var current_place = stories[0].place; 
		var next_place = stories[1].place;

		if (current_place != next_place)
		{
			slideToBounds(current_place, next_place,3000); 
			var current_route = find_routes(current_place,next_place);
			// I know this is clunky, but it works, no time to make it pretty:
			draw_route([{path: current_route.path}]);
		}
		console.log(i);
		setTimeout(function(){
//STORY IS HERE
			console.log(stories[i].evt);
			$("#story").text(stories[i].evt);
		},time_route_draw);

		current_place = next_place;
		i++;

		//loop starts here
		setInterval(function()
			{
				next_place = stories[i+1].place;
				find_coord_of_city(current_place,cities);

				if (current_place != next_place)
				{
					slideToBounds(current_place, next_place, 3000);
					var current_route = find_routes(current_place,next_place);
					// I know this is clunky, but it works, no time to make it pretty:
					draw_route([{path: current_route.path}]);
				}

				setTimeout(function(){
//STORY IS HERE
					console.log(stories[i].evt);
					$("#story").text(stories[i].evt);
				},time_route_draw);

				current_place = next_place;
				i++;
				if (i+1 > stories.length-1)
				{
					current_place = stories[0].place;
					i = 0;
				}
			},time_interval);

		//draw_route([{path: routes[counter].path}])
		//counter++;
			
		/*	
		route = main_svg.selectAll('path').data([{path: routes[0].path}]).enter()
					.append('path')
					.attr('d',function(d){return lineFunction(d.path)})
					.style('stroke','red')
					.style('stroke-width','2pt')
					.style('position','relative')
					.attr('fill','none')
				//					.transition()
									//.duration(5500)
		//route.attrTween("stroke-dasharray",tweenDash)
		*/
	});
	
});

var time_interval = 8000;
var time_route_draw = 2500;

var draw_route = function(path_array){
    main_svg.selectAll('path').remove();
    var drawn_route = main_svg.selectAll('path').data(path_array).enter()
                    .append('path')
                    .attr('d',function(d){return lineFunction(d.path)})
                    .style('stroke','red')
                    .style('stroke-width','2pt')
                    .style('position','relative')
                    .attr('fill','none')

    // use jquery animate, which will animate 'val' from 0 to 1, and
    // then manually set the stroke-array thing to the correct percentate
    // of the full path length at each frame. when it's finished it 
    // disables the stroke-dasharray property, so that the line will always
    // be fully drawn from then on.
    $({foo:0}).animate({foo:1}, {
        duration: time_route_draw,
        step: function(val) {
            main_svg.selectAll('path')
                .style('stroke-dasharray', function(){
                    var len = this.getTotalLength();
                    return (val*len + ', ' + len);
                });
        },
        complete: function() {
            main_svg.selectAll('path')
                .style('stroke-dasharray', 'none');
        }
    });
}


/*
var path = [];
for (var i = 0; i < cities.length; i++)
{
	path.push({lat: cities[i].lat,lon: cities[i].lon});
}
*/
var find_coord_of_city = function(city_name,cities_array)
{
	for (var i = 0; i < cities_array.length; i++)
	{
		if (city_name === cities_array[i].name){
			return {lat: cities_array[i].lat, lon: cities_array[i].lon};
		}
	}
}

var find_routes = function(city1, city2)
{
	for (var i = 0; i < routes.length; i++)
	{
		if (routes[i].origin === city1 && routes[i].destination === city2)
		{			main_svg.selectAll('g').data(cities, function(d){return d.name}).enter().append('g').append('text')
				.attr({
					'x': function(d){return mapToPixel(d.lon,d.lat)[0]},
					'y': function(d){return mapToPixel(d.lon,d.lat)[1]},
					'font-family':'trebuchet',
					'font-size':'18px'
				})
			return routes[i];	
		}
	}
}

        var slideToBounds = function(start, end, animduration) {
            var start = find_coord_of_city(start,cities);
            var end   = find_coord_of_city(end,cities);
            var start_ol =  ol.proj.transform([start.lon,start.lat], 'EPSG:4326', 'EPSG:3857');
            var end_ol   =  ol.proj.transform([end.lon,  end.lat],   'EPSG:4326', 'EPSG:3857');

            var newViewExtent = ol.extent.boundingExtent([start_ol, end_ol]);
            var newView = new ol.View();
            newView.fitExtent(newViewExtent, map.getSize());

            var zoom = ol.animation.zoom({
              resolution: map.getView().getResolution(),
              duration:   animduration
            });
            var pan = ol.animation.pan({
              source:   map.getView().getCenter(),
              duration: animduration
            });

            map.beforeRender(pan, zoom);
            map.setView(newView);
        };




var tweenDash = function tweenDash() {
	//This function is used to animate the dash-array property, which is a
	//  nice hack that gives us animation along some arbitrary path (in this
	//  case, makes it look like a line is being drawn from point A to B)
	var len = this.getTotalLength(),
			interpolate = d3.interpolateString("0," + len, len + "," + len);

	return function(t) { return interpolate(t); };
};

var lineFunction = d3.svg.line()
	.interpolate('basis')
	.x(function(d) {return mapToPixel(d.lon,d.lat)[0]})
	.y(function(d) {return mapToPixel(d.lon,d.lat)[1]})


var routes = [];

routes.push(
	{ origin:	'Sydney',
	  destination: 'Alexandria',
		path: [	{lat: -33.8650, lon: 151.2094},
						{lat:	-33.8312,	lon: 151.8574},	
						{lat:	-31.4312,	lon: 153.3574},	
						{lat:	-26.4312,	lon: 154.3574},	
						{lat:	-21.4312,	lon: 153.8574},	
						{lat:	-11.1745,	lon: 145.8227},	
						{lat:	-10.3149,	lon: 133.4179},	
						{lat:	-11.8673,	lon: 124.4531},	
						{lat:	 -8.7245,	lon: 106.9527},	
						{lat:	 -6.6245,	lon: 105.3809},	// Jakarta
						{lat:	 -4.4654,	lon: 106.7809},	
						{lat:		0.2636,	lon: 105.8000},	//Singapore
						{lat:		1.3000,	lon: 103.8000},	//Singapore
						{lat:		1.8234,	lon: 102.37},	//Singapore
						{lat:	  3.5574,	lon: 100.3491},	
						{lat:	  6.5374,	lon:  96.7675},	
						{lat:	  6.8173,	lon:  92.7975},	
						{lat:	  3.0000, lon:  81.0000},
						{lat:	 13.9600, lon:  52.7343}, // Aden
						{lat:	 12.8000, lon:  45.0333}, // Aden
						{lat:	 11.566, lon:  44.0800},
						{lat:	 27.3132, lon:  34.2553}, 
						{lat:	 29.6689, lon:  32.5857}, 
						{lat:	 31.7655, lon:  31.5307}, 
						{lat:	 31.2000,	lon:  29.9167} ] // Alexandria
	});

/*
routes.push(
	{ origin: 'Alexandria',
		destination: 'Plymouth',
		path: [	{lat:  31.2000, lon: 29.9167},
						{lat:	 37.8312,	lon: 11.5574},	
						{lat:	 36.279,	lon: -1.5874},	
						{lat:	 36.1430,	lon: -5.3530},	
						{lat:	 36.4566,	lon: -9.4921},	
						{lat:	 39.0277,	lon: -10.239},	
						{lat:	 43.8028,	lon: -9.580},	
						{lat:	 48.516,	lon: -5.449},	
						{lat:	50.3714,	lon: -4.1422}	]
	});
*/

routes.push(
	{ origin: 'Alexandria',
		destination: 'Gallipoli',
		path: [	{lat:  31.2000, lon: 29.9167},
						{lat:	 37.1428,	lon: 25.8947},	
						{lat:	 40.2536,	lon: 26.275790} ]
	});

routes.push(
	{ origin: 'Gallipoli',
		destination: 'Alexandria',
		path: [	{lat:  40.2536, lon: 26.275790},
						{lat:	 37.1428,	lon: 25.8947},	
						{lat:	 31.2000, lon: 29.9167} ]
	});

routes.push(
	{ origin: 'Alexandria',
		destination: 'Marseilles',
		path: [	{lat:  31.2000, lon: 29.9167},
												{lat:	 33.6877,	lon: 24.1040},	
						{lat:	 34.1981,	lon: 13.9947},	
						{lat:	 40.2795,	lon: 11.0083},	
						{lat:	 43.3031, lon: 5.3804} ]
	});

routes.push(
	{ origin: 'Marseilles',
		destination: 'Bailleul',
		path: [	{lat:  43.3031, lon: 5.3804},
						{lat:	 46.6020,	lon: 2.846033},	
						{lat:	 50.7387, lon: 2.741930} ]
});

var cities = [   //{name: 'Parramatta', lat:-33.812757, lon: 151.006718},
								 {name: 'Sydney', lat: -33.8650, lon: 151.2094},
								 {name: 'Brisbane', lat: -27.4667, lon: 153.0333},	
								 {name: 'Batavia', lat: -6.1745, lon: 106.8227},	
								 {name: 'Singapore', lat: 1.3000, lon: 103.8000},	
								 {name: 'Ceylon', lat: 7.0000, lon: 81.0000},	
								 {name: 'Aden', lat: 12.8000, lon: 45.0333},	
								 {name: 'Alexandria', lat: 31.2000, lon: 29.9167},	
								 {name: 'Marseilles', lat: 43.3031, lon: 5.3804},	
								 //{name: 'Brezy', lat: 46.6020, lon: 2.846033},	
								 {name: 'Gibraltar', lat: 36.1430, lon: -5.3530},	
								 {name: 'Gallipoli', lat: 40.253634, lon: 26.275790},
								 {name: 'Bailleul', lat: 50.738710, lon: 2.741930},
								 //{name: 'Plymouth', lat:	50.3714,	lon: -4.1422}
						];


	
	
var stories = [];	
stories = 
	[{	place: 'Sydney',
			date:	'12 July 1915',
			evt: 'Enlisted with 4 Rein 20th Battalion in Parramatta'},
		{ place: 'Alexandria',
			date: '4 November 1915',
			evt: 'Embarked with 5 Rein 20th Battalion'},
		{ place: 'Gallipoli',
			date:	'12 November 1915',
			evt: 'Taken on Strength of Bn as Pte and posted to B Company'},
		{ place: 'Alexandria',
		  date: '9 January 1916',
			evt: 'Disembarked off Mudros'},
		{ place: 'Gallipoli',
			date: '28 January 1916',
			evt: 'Appointed Lance Corporal'},
		{ place: 'Alexandria',
			date: '18 March 1916',
			evt: 'Embarked HMT Haverford'},
		{ place: 'Marseilles',
		  date: '25 March 1916',
			evt: 'Disembarked HMT Haverford'},
		{ place: 'Bailleul',
			date: '3 May 1916',
			evt: 'Wounded in action. Gunshot wound, multiple to 8 Cas C Stn. ' + 
						 'Fractured left arm. Admitted.'},
		{ place: 'Bailleul',
			date: '5 May 1916',
			evt: 'Died of wounds. Buried at Bailleul Cemetery. ' +
							'Reported by the Rev AF Fenn'}
	];
		

		  


