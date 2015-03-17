 
use strict;
use warnings;

use CGI;
use JSON;
use Template;

my $q = new CGI;
my $o = new CGI;
my %data;

function suma(q, o) {
  return q+o;
}
# if ( my $number = $q->param('number') && my $numberO = $o->param('numberO') )
# {
#     if ( $number )
#     {
#         $data{result} = $number % 2 ? 'odd' : 'even';
#     }
#     else
#     {
#         $data{result} = 'Not a number';
#     }

#     print $q->header('application/json');
#     print to_json(\%data);
#     exit;
# }

$data{title} = 'Simple jquery example';

print $q->header( -charset=>'utf-8' );
my $tt = Template->new;
$tt->process('simple.tmpl', \%data);