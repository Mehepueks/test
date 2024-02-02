undecided ='''You dont seem to be able to make decisions in life already... Your life has suddenly ended and you will be reincarnated as a human baby\n                      .      .       .       .
  .   .       .          .      . .      .         .          .    .
         .       .         .    .   .         .         .            .
    .   .    .       .         . . .        .        .     .    .
 .          .   .       .       . .      .        .  .              .
      .  .    .  .       .     . .    .       . .      .   .        .
 .   .       .    . .      .    . .   .      .     .          .     .
    .            .    .     .   . .  .     .   .               .
     .               .  .    .  . . .    .  .                 .
                        . .  .  . . .  . .
                            . . . . . .
                              . . . .
                               I . I
                 _______________III_______________
                /    .       .       .       .    \
               ( ~~~ .  ~~~  .  ~~~  .  ~~~  . ~~~ )
                 \SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/
                    \ ======================= /
                        \SSSSSSSSSSSSSSSSS/
                     ________\       /________
                    (=+=+=+=+=+=+=+=+=+=+=+=+=)
                     ~~~~~~~~~~~~~~~~~~~~~~~~~'''

print("Welcome to Life\nYour mission is to not mess up and find sense in your existence.\nGodspeed!")

print('''         .                      .
         .                      ;
         :                  - --+- -
         !           .          !
         |        .             .
         |_         +
      ,  | `.
--- --+-<#>-+- ---  --  -
      `._|_,'
         T
         |
         !
         :         . : 
         .       *''')
name = input('What Name has been given to you?\n')
print(f'Welcome to life {name}')
#Decide if you wanna be poor or rich

#Decided to be rich
rich_or_poor = input('You have just been born. Would you like to be poor or rich?\n')
if rich_or_poor.lower() == 'rich':
  print('You have been born into a rich family, you are now a millionaire')
  druggs_or_goods = input('You have been growing up with no material desires however something seems to be missing..\nDo you want to experiment with drugs or buy yourself more goods to fill that hole? Type "goods" or "drugs"')
  #goods or drugs?
  if druggs_or_goods.lower() == 'drugs':
    print('You have been experimenting with drugs and have been diagnosed with a deadly drug overdose.\n During the overdose you made the promise to yourselve the renounce everything you had and after years of pilgrimage you have finally found your way to the afterlife. You are now dead and will not be reincarnated again')
  elif druggs_or_goods.lower() == 'goods':
    print('You have been spending your life impressing others, but the feling of emptiness has never left you... You will be reincarnated as a caterpilar')
    print('''                                            _     _
                   ,,,,,,,,,,,,,,,,,,,,,,,,  \   /
                 / (  (  (  (  (  (  (  (  \ [ = =]
                <  (  (  (  (  (  (  (  (  /  { ^ }
                 \ (__(__(__(__(__(__(__(__)    ~
                   ^  ^  ^  ^  ^  ^  ^  ^  ^''')
  else: 
    print(undecided)

#Decided to be poor
elif rich_or_poor == 'poor':
  print('You have been born into a poor family, you are now a homeless struggling')
  car_or_accept = input('You have been growing up with the idea that belongins will make you happy one day...\nAre you going to save up for a car you cant afford or will you accept the fact that you will never earn more? Type "car" or "accept"')
  if car_or_accept.lower() == 'car':
    print('You have gotten into the behaviour to reach for things you cannot affford nor maintain, therefore you destroyed your life financially and socialiy to the point where your pain granted you a view into a more complex world.. Your cycle of reincarnation has ended and you will life on as an eternal being')
    print('''
    ` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .
        ` : | :|  ||  |:  :    `  |  | :| : | : |:   |  .                    :
           .' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.
                  `'  ||  |  ' |   *    ` : | | :| |*|  :   :               :|
          *    *       `  |  : :  |  .      ` ' :| | :| . : :         *   :.||
               .`            | |  |  : .:|       ` | || | : |: |          | ||
        '          .         + `  |  :  .: .         '| | : :| :    .   |:| ||
           .                 .    ` *|  || :       `    | | :| | :      |:| |
   .                .          .        || |.: *          | || : :     :|||
          .            .   . *    .   .  ` |||.  +        + '| |||  .  ||`
       .             *              .     +:`|!             . ||||  :.||`
   +                      .                ..!|*          . | :`||+ |||`
       .                         +      : |||`        .| :| | | |.| ||`     .
         *     +   '               +  :|| |`     :.+. || || | |:`|| `
                              .      .||` .    ..|| | |: '` `| | |`  +
    .       +++                      ||        !|!: `       :| |
                +         .      .    | .      `|||.:      .||    .      .    `
            '                           `|.   .  `:|||   + ||'     `
    __    +      *                         `'       `'|.    `:
  "'  `---"""----....____,..^---`^``----.,.___          `.    `.  .    ____,.,-
      ___,--'""`---"'   ^  ^ ^        ^       """'---,..___ __,..---""'
  --"'                           ^                         ``--..,__
''')
  elif car_or_accept.lower() == "accept":
    print('You have never tested yourself and stayed in your line all the way through, which is why you never discovered your true self.\nYou are being reincarnated as a fly')
    print('''        __
   -. (#)(#) .-
    '\.';;'./'
 .-\.'  ;;  './-.
   ;    ;;    ;
   ;   .''.   ;
    '''    '''        ''')
  else:
    print(undecided)
else:
  print(undecided)
  #test