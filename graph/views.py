from django.shortcuts import render_to_response, RequestContext
import facebook

def graph(request):
	graph = facebook.GraphAPI(access_token='CAARaCIX6lTIBALQU8IWkmZBKOOrUnIcrvLN6uzbKrPE89pgZBuP9uHvoZAL2FmJsLoDZA2e1JwcUxuMYzWZCgoZAqKdzAcFg4aLZCbklx6BgrjD6KnlVSPiOZCee6kE2Y0uRJFxPzxDr9sv4YUQEIEPJUxZBhfbLdfRyQSYFcrZB0W0JVV8m9FwtxFVVMPpgzpECHFmv2EHpA9ZBQZDZD', version='2.5')
	
	friends = graph.get_connections(id='944836392265985', connection_name='friends')

	#graph.put_object(parent_object='me', connection_name='feed',
    #             message='Post enviado via app facebook')
	
	print friends

	return render_to_response('graph.html', locals(),context_instance=RequestContext(request)
        )