ckan.module('apihelper', function (jQuery, _) {
  return {
    initialize: function () {
      this.el.change(this.change);
    },
    change: function (e) {
      var helparea = $('#apihelper-help');
      var help_text = "Select an endpoint to see it's documentation.";
      // get element only if it exists
      if(action_help[e.val] !== undefined) {
        help_text = action_help[e.val];
      }
      // get the newlines converted properly
      help_text = help_text.replace(/\n/g, '<br />')
      helparea.html(help_text);
    },
  };
});
ckan.module('apihelper-submit', function (jQuery, _) {
  return {
    initialize: function () {
      this.el.click(this._click);
    },
    _click: function (e) {
      e.preventDefault();
      var action = $('#field-actions option:selected')[0].value;
      var output = '';
      if(action_help[action] === undefined) {
        return
      }
      var r = $.get(ckan.SITE_ROOT + '/api/3/action/' + action, function(data) {
        var output_area = $('#apihelper-output');
        output_area.text(JSON.stringify(data, null, "\t"));
      });
      r.fail(function(data) {
        console.log('failed with %o', data);
      });
    },
  };
});
