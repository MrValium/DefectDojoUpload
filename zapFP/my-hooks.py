import logging

def zap_get_alerts(zap, baseurl, denylist, out_of_scope_dict):
    st = 0
    pg = 5000
    false_positives = [[10096, 'http://example.com'],[10021,'http://192.168.49.2:31190/swagger-ui/swagger-ui.css'],[10038,'http://192.168.49.2:31190/'],[10038,'http://192.168.49.2:31190']]
    alerts = zap.core.alerts(baseurl=baseurl, start=st, count=pg)
    alert_dict = {}
    alert_count = 0
    found=0
    while len(alerts) > 0:
        logging.debug('Reading AAAA ' + str(pg) + ' alerts from ' + str(st))
        alert_count += len(alerts)
        for alert in alerts:
            found=0
            alert_id = alert.get('id')
            url = alert.get('url')
            plugin_id = alert.get('pluginId')
            for fp in false_positives:
                logging.debug('BBBBBBBBB' +str(fp[0])+'---'+str(fp[1]))
                if (plugin_id == fp[0] and url == fp[1]):
                    zap.alert.update_alerts_confidence(alert_id, '0')
                    found=1
            if (plugin_id not in alert_dict and found==0):
                alert_dict[plugin_id] = []
            if (found==0):
                alert_dict[plugin_id].append(alert)
            st += pg
            alerts = zap.core.alerts(start=st, count=pg)
    logging.debug('Total number of alerts: ' + str(alert_count))
    return alert_dict
